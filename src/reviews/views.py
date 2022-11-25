from itertools import chain

from django.contrib.auth.decorators import login_required
from django.db.models import Value
from django.forms import CharField
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from authentication.models import User, UserFollows
from reviews import models, forms
from reviews.forms import ReviewForm
from tickets.forms import TicketForm
from reviews.models import Review
from tickets.models import Ticket


class ArticleListView(ListView):
    model = Review
    template_name = "feed_2.html"


@login_required
def feed(request):
    followers = request.user.following.all()
    followers_id = []
    for follower in followers:
        followers_id.append(follower.followed_user.pk)

    ticket_id_answers = []
    for ticket in models.Ticket.objects.filter(user=request.user):
        for review in models.Review.objects.all():
            if review.ticket == ticket:
                ticket_id_answers.append(review.user.pk)
    reviews = (
            models.Review.objects.filter(user=request.user)
            | models.Review.objects.filter(user_id__in=followers_id)
            | models.Review.objects.filter(user_id__in=ticket_id_answers)
    )
    reviews = reviews.annotate(content_type=Value('REVIEW'))

    tickets = models.Ticket.objects.filter(user=request.user) | models.Ticket.objects.filter(user_id__in=followers_id)
    tickets = tickets.annotate(content_type=Value('TICKET'))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    context = {
        'posts': posts,
    }
    return render(request, 'feed.html', context=context)


def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', context={'review': review})


def review_add(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.has_review = True
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('review-detail', review.id)
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'review_add.html', context=context)


def review_answer(request, ticket_id):
    existing_ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form_review = forms.ReviewForm()
    if request.method == 'POST':
        form_review = forms.ReviewForm(request.POST)
        if form_review.is_valid():
            existing_ticket.has_review = True
            existing_ticket.save()
            review = form_review.save(commit=False)
            review.user = request.user
            review.ticket = existing_ticket
            review.save()
            return redirect('posts')
    context = {
        'form_review': form_review,
        'existing_ticket': existing_ticket
    }
    return render(request, 'review_answer.html', context=context)


def review_update(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    update_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'review_update' in request.POST:
            update_form = forms.ReviewForm(request.POST, request.FILES, instance=review)
            if update_form.is_valid():
                update_form.save()
                return redirect('posts')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.ticket.no_review()
                review.ticket.save()
                review.delete()
                return redirect('posts')
    context = {
        'update_form': update_form,
        'delete_form': delete_form,
    }
    return render(request, 'review_update.html', context=context)


def posts_page(request):
    reviews = Review.objects.filter(user=request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', ))

    tickets = Ticket.objects.filter(user=request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', ))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'posts.html', context={'posts': posts})


def unfollow(request, user_follow_id):

    UserFollows.objects.get(id=user_follow_id).delete()

    return redirect('subscription')

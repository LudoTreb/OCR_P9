from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from reviews.forms import ReviewForm
from tickets.forms import TicketForm
from reviews.models import Review
from tickets.models import Ticket


class ArticleListView(ListView):
    model = Review
    template_name = "feed_2.html"


@login_required
def feed(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    return render(request, 'feed.html', context={'reviews': reviews,
                                                 'tickets': tickets})


def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', context={'review': review})


def review_add(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
        review_form = ReviewForm(request.POST)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
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


# def review_answer(request, ticket_id):
#     ticket = Ticket.objects.get(id=ticket_id)
#     review_form = ReviewForm
#     if request.method == 'POST':
#         review_form = ReviewForm(request.POST)
#         if review_form.is_valid():
#             review = review_form.save(commit=False)
#             review.user = request.user
#             review.save()
#             return redirect('review-answer', review.id)
#     else:
#         ticket = Ticket.objects.get(id=ticket_id)
#         review_form = ReviewForm()
#
#     context = {
#         'ticket': ticket,
#         'review_form': review_form,
#     }
#     return render(request, 'review_answer.html', context=context)

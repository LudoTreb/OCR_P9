from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from reviews.forms import ReviewForm
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
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('review-detail', review.id)
    else:
        form = ReviewForm()
    return render(request, 'review_add.html', {'form': form})

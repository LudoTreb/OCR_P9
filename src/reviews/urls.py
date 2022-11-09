from django.contrib.auth.decorators import login_required
from django.urls import path

from reviews.views import feed, ArticleListView, review_add, review_detail

urlpatterns = [
    # path("flux/", login_required(ArticleListView.as_view()), name="reviews"),
    path("", feed, name="home"),
    path("review/add/", review_add, name="review-add"),
    path("review/<int:review_id>/", review_detail, name="review-detail"),
]

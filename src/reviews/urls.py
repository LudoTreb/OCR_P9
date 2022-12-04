"""
Urls for the review.
"""
from django.urls import path

from reviews.views import (
    feed,
    review_add,
    review_detail,
    review_answer,
    posts_page,
    review_update,
    unfollow,
)

urlpatterns = [
    path("", feed, name="home"),
    path("review/add/", review_add, name="review-add"),
    path("review/<int:ticket_id>/answer/", review_answer, name="review-answer"),
    path("posts/", posts_page, name="posts"),
    path("review/<int:review_id>/", review_detail, name="review-detail"),
    path("review/<int:review_id>/update", review_update, name="review-update"),
    path("unfollow/<int:user_follow_id>/", unfollow, name="unfollow"),
]

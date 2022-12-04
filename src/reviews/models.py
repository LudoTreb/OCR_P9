"""
The model for the review.
"""

from django.db import models

from LITReview.settings import AUTH_USER_MODEL
from tickets.models import Ticket


class Review(models.Model):
    """
    A review model. The user can input a headline, a rating and a review.
    """

    class Rating(models.TextChoices):
        """
        The choice of rating.
        """

        ZERO_ETOILE = "0"
        UNE_ETOILE = "1"
        DEUX_ETOILES = "2"
        TROIS_ETOILES = "3"
        QUATRE_ETOILES = "4"
        CINQ_ETOILES = "5"

    ticket = models.ForeignKey(
        to=Ticket, on_delete=models.CASCADE, null=True, blank=True
    )
    headline = models.CharField(max_length=128, verbose_name="Avis")
    rating = models.fields.CharField(
        choices=Rating.choices, max_length=5, default="5", verbose_name="Note"
    )
    body = models.TextField(max_length=8192, default="", verbose_name="Commentaire")
    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

from django.db import models

from LITReview.settings import AUTH_USER_MODEL
from tickets.models import Ticket


class Review(models.Model):
    class Rating(models.TextChoices):
        zéro_étoile = '0'
        une_étoile = '1'
        deux_étoiles = '2'
        trois_étoiles = '3'
        quatre_étoiles = '4'
        cinq_étoiles = '5'

    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True, blank=True)
    headline = models.CharField(max_length=128, verbose_name='Avis')
    rating = models.fields.CharField(choices=Rating.choices, max_length=5, default='5', verbose_name='Note')
    body = models.TextField(max_length=8192, default="", verbose_name='Commentaire')
    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

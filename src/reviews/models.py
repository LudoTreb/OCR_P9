from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
from LITReview.settings import AUTH_USER_MODEL
from tickets.models import Ticket


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True, blank=True)
    headline = models.CharField(max_length=128)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    body = models.TextField(max_length=8192, default="")
    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

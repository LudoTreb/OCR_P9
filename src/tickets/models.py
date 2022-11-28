from django.db import models

# Create your models here.
from django.db.models import DateTimeField, ImageField

from LITReview.settings import AUTH_USER_MODEL


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name="titre")
    description = models.TextField(max_length=2048, blank=True, default="")
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    time_created = DateTimeField(auto_now_add=True)
    has_review = models.BooleanField(blank=True, default=False)

    def no_review(self):
        self.has_review = False

    def is_book_or_article(self):
        pass

    def resize_img(self):
        pass


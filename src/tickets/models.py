"""
The model for the ticket.
"""

from PIL import Image
from django.db import models
from django.db.models import DateTimeField

from LITReview.settings import AUTH_USER_MODEL


class Ticket(models.Model):
    """
    Ticket model. User can input a title, a description and upload an image.
    """

    title = models.CharField(max_length=128, verbose_name="titre")
    description = models.TextField(max_length=2048, blank=True, default="")
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(
        to=AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    time_created = DateTimeField(auto_now_add=True)
    has_review = models.BooleanField(blank=True, default=False)

    IMAGE_MAX_SIZE = (220, 220)

    def resize_img(self):
        """
        Automatically resizes the image (220X220) as soon as it is uploaded.
        """
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        """
        Automatically save the image if an image has been uploaded.
        """
        super().save(*args, **kwargs)
        if self.image:
            self.resize_img()

    def no_review(self):
        """
        Define if ticket has review or not
        """
        self.has_review = False

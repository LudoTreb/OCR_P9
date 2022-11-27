from django.db import models


# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    # TODO: To implement?
    # Image download ?
    # User
    # Quand ?

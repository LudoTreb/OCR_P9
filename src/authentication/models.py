# TODO: use isort to sort libs automatically
from django.db import models
from django.contrib.auth.models import AbstractUser

# TODO: delete unused comment
# Create your models here.
class User(AbstractUser):
    profil_picture = models.ImageField()

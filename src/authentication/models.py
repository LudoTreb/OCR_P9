from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from LITReview.settings import AUTH_USER_MODEL


class User(AbstractUser):
    profil_picture = models.ImageField()

    def __str__(self):
        return f'{self.username}'


class UserFollow(models.Model):
    class Meta:
        unique_together = ['user', 'followed_user']

    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    def __str__(self):
        return f'{self.username}'

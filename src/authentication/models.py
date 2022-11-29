from django.contrib.auth.models import AbstractUser
from django.db import models

from LITReview.settings import AUTH_USER_MODEL


class User(AbstractUser):
    profil_picture = models.ImageField()
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suivre',
    )

    def __str__(self):
        return f'{self.username}'


class UserFollows(models.Model):
    class Meta:
        unique_together = ['user', 'followed_user']

    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    def __str__(self):
        return f'{self.followed_user.username}'

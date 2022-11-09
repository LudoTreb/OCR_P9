from django.db import models


# Create your models here.
class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE_STAR = 1
        TWO_STAR = 2
        THREE_STAR = 3
        FOUR_STAR = 4
        FIVE_STAR = 5

    title = models.CharField(max_length=100)
    rating = models.IntegerField(choices=Rating.choices, default=5)
    comment = models.TextField(default="")
    # user
    # time_created = models.DateTimeField(auto_now_add=True)

    # integrer les tickets ?

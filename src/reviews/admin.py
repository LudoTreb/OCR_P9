"""
The review for administrator.
"""
from django.contrib import admin

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    The review's model for the administrator.
    With the fields ticket, rating, headline, body, time_created
    """

    list_display = ("ticket", "rating", "headline", "body", "time_created")


admin.site.register(Review, ReviewAdmin)

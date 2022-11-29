from django.contrib import admin

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'rating', 'headline', 'body', 'time_created')


admin.site.register(Review, ReviewAdmin)

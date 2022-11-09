from django.contrib import admin

# Register your models here.
from reviews.models import Review


class CriticAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'comment')


admin.site.register(Review, CriticAdmin)

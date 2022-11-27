from django.contrib import admin

# TODO: remove comment if not useful
# Register your models here.
from reviews.models import Review


class CriticAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'comment')


admin.site.register(Review, CriticAdmin)

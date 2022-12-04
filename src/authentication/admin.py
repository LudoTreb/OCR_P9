"""
The account for administrator.
"""
from django.contrib import admin
from django.contrib.auth import get_user_model

from authentication.models import UserFollows

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    """
    The user model for the administrator with the field username.
    """

    list_display = ("username",)


class UserFollowAdmin(admin.ModelAdmin):
    """
    The user follow model for the administrator with fields user and followed user.
    """

    list_display = ("followed_user", "user")


admin.site.register(User, UserAdmin)
admin.site.register(UserFollows, UserFollowAdmin)

from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from authentication.models import UserFollow

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ()


class UserFollowAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(User, UserAdmin)
admin.site.register(UserFollow, UserFollowAdmin)

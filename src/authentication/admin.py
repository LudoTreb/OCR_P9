from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from authentication.models import UserFollows

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)


class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('followed_user', 'user')


admin.site.register(User, UserAdmin)
admin.site.register(UserFollows, UserFollowAdmin)

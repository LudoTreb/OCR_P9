"""
Urls for the different ection of the user. Login, signup, subscription.
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from authentication.views import signup_page, subscriptions

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="login.html", redirect_authenticated_user=True),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("subscription/", subscriptions, name="subscription"),
    path("signup/", signup_page, name="signup"),
]

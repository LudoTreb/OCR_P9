from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
# TODO: Add empty line between third part libraries and project files/modules
from authentication.views import signup_page

urlpatterns = [
    # TODO: remove empty line
    path("login/", LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('signup/', signup_page, name='signup')
    # TODO: remove empty line
]

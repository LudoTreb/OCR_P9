from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from django.views.generic import View

from authentication import forms, models
from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

from authentication.models import User, UserFollows


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'signup.html', context={'form': form})


def subscriptions(request):
    current_user = request.user
    users = User.objects.all()
    user_follows = models.UserFollows.objects.all()
    subscribers = current_user.followed_by.all()
    if request.method == "POST":
        entry = request.POST["followed_user"]

        if entry == current_user.username:
            return redirect("subscription")

        for user in user_follows:
            if (user.followed_user.username == entry) and (
                    user.user.username == current_user.username
            ):
                return redirect("subscription")

        for user in users:
            if user.username == entry:
                user_to_follow = User.objects.get(username=entry)
                models.UserFollows.objects.create(
                    user=current_user, followed_user=user_to_follow
                )

                return redirect("subscription")

        return redirect("subscription")

    else:
        form = forms.SubscriptionsForm()

    context = {
        "form": form,
        "current_user": current_user,
        "subscribers": subscribers,
        "user_follows": user_follows,
    }
    return render(request, "subscription.html", context=context)

# def logout_user(request):
#     logout(request)
#     return redirect('login')


# def login_page(request):
#     form = LoginForm()
#     message = ""
#     if request.method == 'POST':
#         print(request.POST)
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 message = "Identifiants invalides."
#
#     return render(request, 'login.html', context={'form': form, 'message': message})


# class LoginPageView(View, LoginRequiredMixin):  # LoginRequiredMixin --> limite l'acces aux connectés
#     form_class = forms.LoginForm
#     template_name = 'login.html'
#
#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Identifiants invalides.'
#         return render(request, self.template_name, context={'form': form, 'message': message})
#
#         return

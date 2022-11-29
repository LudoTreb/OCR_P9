from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authentication import forms, models
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


@login_required
def subscriptions(request):
    current_user = request.user
    users = User.objects.all()
    user_follows = models.UserFollows.objects.all()
    subscribers = current_user.followed_by.all()
    if request.method == "POST":
        entry = request.POST["followed_user"]

        if not User.objects.filter(username=entry).exists():
            messages.error(request, "n'existe pas")
        try:
            user = User.objects.get(username=entry)
            UserFollows.objects.create(
                user=current_user, followed_user=user
            )
        except User.DoesNotExist:
            pass

    form = forms.SubscriptionsForm()

    context = {
        "form": form,
        "current_user": current_user,
        "subscribers": subscribers,
        "user_follows": user_follows,
    }
    return render(request, "subscription.html", context=context)

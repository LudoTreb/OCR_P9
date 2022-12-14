"""
Views for signup and subscriptions.
"""
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authentication import forms, models
from authentication.models import User, UserFollows


def signup_page(request):
    """
    Display the signup page, to allow the user to create his account

    **Context**
    ``form``
        An instance of : `forms.SignupForm`.

    **Template:**
    template: `signup.html'
    """
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "signup.html", context={"form": form})


@login_required
def subscriptions(request):
    """
    Display the subscription page. The user can search another user to follow.
    He can also unfollow and see wich user follow him.

    **Context**
    ``form``
        An instance of : `forms.SubscriptionsForm`.
    ``current_user``
        An instance of : `forms.SubscriptionsForm`.
    ``subscribers``
        A Queryset of : `current_user.followed_by.all()`.
    ``user_follows``
        A Queryset of : `models.UserFollows.objects.all()`.

    **Template:**
    template: `subscription.html'
    """
    current_user = request.user
    user_follows = models.UserFollows.objects.all()
    subscribers = current_user.followed_by.all()
    if request.method == "POST":
        entry = request.POST["followed_user"]

        if not User.objects.filter(username=entry).exists():
            messages.error(request, "n'existe pas")
        try:
            user = User.objects.get(username=entry)
            UserFollows.objects.create(user=current_user, followed_user=user)
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

"""
The form for the user to login, signup and follow other user.
"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from authentication.models import User, UserFollows


class LoginForm(forms.Form):
    """
    The login's form. Ask user his username and password.
    """

    username = forms.CharField(max_length=30, label="Nom d'utilisateur")
    password = forms.CharField(
        min_length=6, widget=forms.PasswordInput, label="Mot de passe"
    )


class SignupForm(UserCreationForm):
    """
    The signup's form. Ask user to choose a username and a password.
    """

    class Meta(UserCreationForm.Meta):
        """
        The signup'model.
        """

        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None


class FollowUsersForm(forms.ModelForm):
    """
    The user follow's form.
    """

    class Meta:
        """
        The user follow's model.
        """

        model = User
        fields = ["follows"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields["follows"].initial)


class SubscriptionsForm(forms.ModelForm):
    """
    The subscription's form.
    """

    class Meta:
        """
        The subscription's model.
        """

        model = UserFollows
        fields = ["followed_user"]
        labels = {"followed_user": ""}
        widgets = {"followed_user": forms.TextInput()}

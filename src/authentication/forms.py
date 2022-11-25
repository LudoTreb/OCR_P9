from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from authentication.models import User, UserFollows


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Nom d'utilisateur")
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label="Mot de passe")


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # Si l'on veut personnalisé les informations que l'on récupérer lors de l'inscription
        # fields = ('username', 'email', 'first_name', 'last_name', 'role')


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']

    def __init__(self, *args, **kwargs):
        super(FollowUsersForm, self).__init__(*args, **kwargs)
        print(self.fields['follows'].initial)


class SubscriptionsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ["followed_user"]
        labels = {"followed_user": ""}
        widgets = {"followed_user": forms.TextInput()}

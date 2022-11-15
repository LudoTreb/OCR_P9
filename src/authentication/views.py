from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from django.views.generic import View

from authentication import forms
from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login, logout


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'signup.html', context={'form': form})


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

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import forms
class RegistrationView(CreateView):
    success_url = '/users/'
    form_class = forms.RegistrationForm
    #form_class = UserCreationForm
    template_name = 'users_app/registration.html'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users_app/login.html'
    success_url = '/add-tvshow/'


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'users_app/user_list.html'

    def get_queryset(self):
        return User.objects.all()
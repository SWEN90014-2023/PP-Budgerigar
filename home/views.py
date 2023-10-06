from django.shortcuts import render
from django.http import HttpResponse
from admin_volt_pro.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
from django.urls import reverse_lazy

# Create your views here.

class UserLoginView(LoginView):
  form_class = LoginForm
  template_name = 'login.html'
  next_page = '/home'

def homePage(request):
    return render(request, "home.html")

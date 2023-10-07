from django.shortcuts import redirect, render
from django.http import HttpResponse
from admin_volt_pro.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout

# Create your views here.

class UserLoginView(LoginView):
  form_class = LoginForm
  template_name = 'login.html'
  next_page = '/dashboard'

def homePage(request):
    return render(request, "includes/navigation.html")

def logout_view(request):
    django_logout(request)
    return redirect('/login')


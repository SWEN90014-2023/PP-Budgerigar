from django.shortcuts import render
from django.http import HttpResponse
from admin_volt_pro.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django import forms
from django.shortcuts import render
from .models import DailyUnlock
from .forms import DateForm
import json

# Create your views here.

class UserLoginView(LoginView):
  form_class = LoginForm
  template_name = 'login.html'
  next_page = '/home'

def homePage(request):
    return render(request, "home.html")

def chart_view(request):
    form = DateForm(request.GET or None)
    chart_data = None
    if form.is_valid():
        selected_date = form.cleaned_data['date']
        try:
            daily_unlock = DailyUnlock.objects.get(date=selected_date)
            chart_data = {
                'categories': ['0-2', '3-5', '6-8', '9-11', '12-14', '15-17', '18-20', '21-23'],
                'series': [{
                    'name': 'Unlocks',
                    'data': [
                        daily_unlock.unlocks_0_2,
                        daily_unlock.unlocks_3_5,
                        daily_unlock.unlocks_6_8,
                        daily_unlock.unlocks_9_11,
                        daily_unlock.unlocks_12_14,
                        daily_unlock.unlocks_15_17,
                        daily_unlock.unlocks_18_20,
                        daily_unlock.unlocks_21_23
                    ]
                }]
            }
        except DailyUnlock.DoesNotExist:
            pass  # Handle the case where the data does not exist
    return render(request, 'chart.html', {
        'form': form,
        'chart_data': json.dumps(chart_data) if chart_data else None,
    })

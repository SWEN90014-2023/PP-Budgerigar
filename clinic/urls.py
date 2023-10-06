from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from . import views

urlpatterns =[
    path('', lambda request: redirect('/login', permanent=False)),
    path('login', views.Login_view, name='login_view'),
    path('home', views.Home_view, name='clinic_home_view'),
    path('patientslist', views.PatientsList_view, name='clinic_patientslist_view')
]

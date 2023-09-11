from django.urls import path
from . import views

urlpatterns =[
    path('',views.Login_view),
    path('home',views.Home_view),
    path('patientslist',views.PatientsList_view)
]
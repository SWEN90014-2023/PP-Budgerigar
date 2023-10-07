from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path('', lambda request: redirect('/login', permanent=False)),
    path('login', views.UserLoginView.as_view(), name='login_view'),
    path('logout', views.logout_view, name="logout2"),
    path('home', views.homePage, name='home_page'),
]

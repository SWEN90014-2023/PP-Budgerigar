from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: redirect('/login', permanent=False)),
    path('login', views.UserLoginView.as_view(), name='login_view'),
    path('logout', views.logout_view, name="logout2"),
    path('home', views.homePage, name='home_page'),
    path('home/get_all_patients/', views.get_all_patients, name='get_all_patients'),
    path('home/addClient/', views.add_client_view, name='add_client'),  
    path('savePatient/', views.save_patient, name='save_patient'),
    path('viewPatient/', views.view_patient, name='view_patient'),
    path('delete_patient/<int:pa_id>/', views.delete_patient, name='delete_patient'),
    path('chart/', views.chart_view, name='chart_view'),  # Add this line to the existing urlpatterns list
]

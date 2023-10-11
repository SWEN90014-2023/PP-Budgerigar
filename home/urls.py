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
    path('get_patient_by_name/<int:clinician_id>/<str:name>/', views.get_patient_by_name, name='get_patient_by_name'),
    ##path('chart/<str:device_id>/',views.chart_view, name='chart_view'),
    path('chartView/',views.chart_view, name='chart_view'),
    path('dailyUnlock/',views.daily_unlock,name='daily_unlock'),
    path('get_date/', views.get_date, name='get_date'),
    path('daily_duration/', views.daily_duration, name='daily_duration'),
]

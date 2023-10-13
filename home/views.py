from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from admin_volt_pro.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from clinic.models import PatientInfo
from django.http import JsonResponse
from django.urls import reverse_lazy
from django import forms
from django.shortcuts import render
from .models import DailyDuration, DailyUnlock, WeeklyDuration, WeeklyUnlock
from .forms import DateForm, WeekForm, get_available_dates, get_available_weeks
from datetime import datetime
import json
from .forms import PatientForm

# Create your views here.

class UserLoginView(LoginView):
  form_class = LoginForm
  template_name = 'login.html'
  next_page = '/dashboard'

def homePage(request):
    return render(request, "homepage/index.html")

def logout_view(request):
    django_logout(request)
    return redirect('/login')

def add_client_view(request):
    # your logic here
    return render(request, 'homepage/addPatient.html')

def get_all_patients(request):
    # Get the current page number, default is 1
    page = int(request.GET.get('page', 1))
    
    # The number displayed on each page can be adjusted as needed
    items_per_page = 5
    
    # Calculate start and end points based on page number and quantity per page
    start_index = (page - 1) * items_per_page
    end_index = page * items_per_page
    
    patients = PatientInfo.objects.all()[start_index:end_index]
    total_patients = PatientInfo.objects.count()
    total_pages = (total_patients - 1) // items_per_page + 1

    # Convert queryset to list of dictionaries
    patient_list = [{
        'pa_id': patient.pa_id,
        'pa_name': patient.pa_name,
        'age': patient.age,
        'sex': patient.sex,
        'info': patient.info,
        'create_time': patient.create_time,
        'device_id':patient.device_id,
    } for patient in patients]

    # Return JSON data
    return JsonResponse({
        'patient_list': patient_list,
        'total_pages': total_pages
    })

def save_patient(request):
    if request.method == "POST":
        pa_name = request.POST.get('pa_name')
        pa_psw = request.POST.get('pa_psw')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        info = request.POST.get('info')
        device_id = request.POST.get('device_id')
        cli_id = request.user.id  # Get the ID of the currently logged in user

        patient = PatientInfo(
            cli_id=cli_id,
            pa_name=pa_name,
            pa_psw=pa_psw,
            age=age,
            sex=sex,
            info=info,
            device_id=device_id
        )
        patient.save()
        
    return redirect('home_page')


def view_patient(request, patient_id):
    patient = get_object_or_404(PatientInfo, pa_id=patient_id)
    
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('view_patient', patient_id=patient.pa_id)
    else:
        form = PatientForm(instance=patient)
    
    return render(request, 'homepage/viewPatient.html', {'patient': patient, 'form': form})


def delete_patient(request, pa_id):
    try:
        patient = PatientInfo.objects.get(pk=pa_id)
        patient.delete()
        return JsonResponse({"success": True, "message": "Patient deleted successfully."})
    except PatientInfo.DoesNotExist:
        return JsonResponse({"success": False, "message": "Patient not found."}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error: {str(e)}"}, status=500)
   
def get_patient_by_name(request, clinician_id, name):
    # get patients
    matching_patients = PatientInfo.objects.filter(pa_name__icontains=name, cli_id=clinician_id)
    
    patients_list = list(matching_patients.values())

    return JsonResponse(patients_list, safe=False)

def chart_view(request):
    return render(request, "chartView/index.html")

def get_date(request):
    device_id = request.GET.get('device_id')
    available_dates = get_available_dates(device_id)
    response_data = {
        'available_dates': available_dates,
    }
    return JsonResponse(response_data)

def get_week(request):
    device_id = request.GET.get('device_id')
    available_weeks = get_available_weeks(device_id)
    response_data = {
        'available_weeks': available_weeks,
    }
    return JsonResponse(response_data)

def daily_unlock(request):
    chart_data = None
    device_id = request.GET.get('device_id')
    print(device_id)
    form = DateForm(request.GET or None, device_id=device_id)
    form_errors = {}
    if form.is_valid():
        selected_date = form.cleaned_data['date']
        try:
            daily_unlock = DailyUnlock.objects.get(date=selected_date, device_id=device_id)
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
            pass
    else:
        # Collect form errors if the form is not valid
        form_errors = {field: errors for field, errors in form.errors.items()}
    
    response_data = {
        'form_errors': form_errors,
        'chart_data': chart_data if chart_data else None,
    }
    print(response_data)
    return JsonResponse(response_data)

def daily_duration(request):
    device_id = request.GET.get('device_id')
    form = DateForm(request.GET or None, device_id=device_id)
    chart_data = None
    form_errors = {}

    if form.is_valid():
        selected_date = form.cleaned_data['date']
        try:
            daily_duration = DailyDuration.objects.get(date=selected_date, device_id=device_id)
            chart_data = {
                'categories': ['0-2', '3-5', '6-8', '9-11', '12-14', '15-17', '18-20', '21-23'],
                'series': [{
                    'name': 'Screen Time',
                    'data': [
                        round(daily_duration.duration_0_2 / 60, 2),
                        round(daily_duration.duration_3_5 / 60, 2),
                        round(daily_duration.duration_6_8 / 60, 2),
                        round(daily_duration.duration_9_11 / 60, 2),
                        round(daily_duration.duration_12_14 / 60, 2),
                        round(daily_duration.duration_15_17 / 60, 2),
                        round(daily_duration.duration_18_20 / 60, 2),
                        round(daily_duration.duration_21_23 / 60, 2)
                    ]
                }]
            }
        except DailyDuration.DoesNotExist:
            pass
    else:
        form_errors = {field: errors for field, errors in form.errors.items()}

    response_data = {
        'form_errors': form_errors,
        'chart_data': chart_data if chart_data else None,
    }
    return JsonResponse(response_data)

def weekly_unlock(request):
    device_id = request.GET.get('device_id')
    form = WeekForm(request.GET or None, device_id=device_id)
    chart_data = None
    form_errors = {}

    if form.is_valid():
        week_start_date = form.cleaned_data['week_start_date']
        try:
            weekly_unlock = WeeklyUnlock.objects.get(week_start=week_start_date, device_id=device_id)
            chart_data = {
                'categories': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                'series': [{
                    'name': 'Unlocks',
                    'data': [
                        weekly_unlock.Monday,
                        weekly_unlock.Tuesday,
                        weekly_unlock.Wednesday,
                        weekly_unlock.Thursday,
                        weekly_unlock.Friday,
                        weekly_unlock.Saturday,
                        weekly_unlock.Sunday
                    ]
                }]
            }
        except WeeklyUnlock.DoesNotExist:
            pass
    else:
        form_errors = {field: errors for field, errors in form.errors.items()}
    
    response_data = {
        'form_errors': form_errors,
        'chart_data': chart_data if chart_data else None,
    }
    return JsonResponse(response_data)

def weekly_duration(request):
    device_id = request.GET.get('device_id')
    form = WeekForm(request.GET or None, device_id=device_id)
    chart_data = None
    form_errors = {}

    if form.is_valid():
        week_start_date = form.cleaned_data['week_start_date']
        try:
            weekly_duration = WeeklyDuration.objects.get(week_start=week_start_date, device_id=device_id)
            chart_data = {
                'categories': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                'series': [{
                    'name': 'Screen Time',
                    'data': [
                        int(weekly_duration.Monday / 60),
                        int(weekly_duration.Tuesday / 60),
                        int(weekly_duration.Wednesday / 60),
                        int(weekly_duration.Thursday / 60),
                        int(weekly_duration.Friday / 60),
                        int(weekly_duration.Saturday / 60),
                        int(weekly_duration.Sunday / 60)
                    ]
                }]
            }
        except WeeklyDuration.DoesNotExist:
            pass
    else:
        form_errors = {field: errors for field, errors in form.errors.items()}
    
    response_data = {
        'form_errors': form_errors,
        'chart_data': chart_data if chart_data else None,
    }
    return JsonResponse(response_data)
from django.shortcuts import render
from django.http import HttpResponse
from admin_volt_pro.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from clinic.models import PatientInfo
from django.http import JsonResponse


=======
from django.urls import reverse_lazy
from django import forms
from django.shortcuts import render
from .models import DailyUnlock
from .forms import DateForm
import json
>>>>>>> a93501db4756245606dbd53419944c1679d911ed

# Create your views here.

class UserLoginView(LoginView):
  form_class = LoginForm
  template_name = 'login.html'
  next_page = '/home'

def homePage(request):
<<<<<<< HEAD
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

def view_patient(request):
    patient_id = request.GET.get('patientId')
    patient = PatientInfo.objects.get(pa_id=patient_id)
    return render(request, 'homepage/viewPatient.html', {'patient': patient})


def delete_patient(request, pa_id):
    try:
        patient = PatientInfo.objects.get(pk=pa_id)
        patient.delete()
        return JsonResponse({"success": True, "message": "Patient deleted successfully."})
    except PatientInfo.DoesNotExist:
        return JsonResponse({"success": False, "message": "Patient not found."}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error: {str(e)}"}, status=500)


=======
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
>>>>>>> a93501db4756245606dbd53419944c1679d911ed

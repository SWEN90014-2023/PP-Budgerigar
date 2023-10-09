from django.shortcuts import redirect, render
from django.http import HttpResponse
from admin_volt_pro.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from clinic.models import PatientInfo
from django.http import JsonResponse



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



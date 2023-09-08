from django.shortcuts import render
from django.http import HttpResponse
from .models import ClinicianInfo, PatientInfo

# Create your views here.

def Login_view(request):
    return render(request, "login.html")

def Home_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')

    if u and p:
        try:
            clinician = ClinicianInfo.objects.get(cli_name=u, cli_psw=p)
            request.session['cli_id'] = clinician.cli_id
            return render(request, 'home.html', {'username': u})
        except ClinicianInfo.DoesNotExist:
            return HttpResponse("Username or password is not correct")
    else:
        return HttpResponse("Please input username and password")

def PatientsList_view(request):
    cli_id = request.session.get('cli_id')
    if cli_id:
        patients = PatientInfo.objects.filter(cli_id=cli_id)
        return render(request, 'patientslist.html', {'patients': patients})
    else:
        return HttpResponse("You are not logged in.")

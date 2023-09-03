from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def toLogin_view(request):
    return render(request, "login.html")

def Login_view(request):
    u = request.POST.get("user",'')
    p = request.POST.get("pwd", '')

    if u and p:
        c = ClinicianInfo.objects.filter(cli_name=u, cli_psw=p).count()
        if c >= 1:
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Username or password is not correct")
    else:
        return HttpResponse("Please input username and password")

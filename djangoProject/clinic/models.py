from django.db import models
import datetime
# Create your models here.

class ClinicianInfo(models.Model):
    cli_id = models.CharField(primary_key=True,max_length=6)
    cli_name = models.CharField(max_length=32)
    cli_psw = models.CharField(max_length=32)
    def __str__(self):
        return 'Clinician_name: {}'.format(self.cli_name)

class PatientInfo(models.Model):
    pa_id = models.CharField(primary_key=True, max_length=6)
    cli_id = models.CharField(max_length=6,default=00)
    pa_name = models.CharField(max_length=32)
    pa_psw = models.CharField(max_length=32)
    age = models.SmallIntegerField(default=0)
    sex = models.CharField(choices=(('Male','Male'), ('Female','Female')), max_length=6, default="Male")
    info = models.TextField()
    create_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return 'patient_name: {}'.format(self.pa_name)

# class AdminInfo(models.Model):
#     ad_name = models.CharField(max_length=32)
#     ad_psw = models.CharField(max_length=32)
#     def __str__(self):
#         return 'admin_name: {}'.format(self.ad_name)
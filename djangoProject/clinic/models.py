from django.db import models

# Create your models here.

class ClinicianInfo(models.Model):
    cli_id = models.CharField(primary_key=True,max_length=6)
    cli_name = models.CharField(max_length=32)
    cli_psw = models.CharField(max_length=32)
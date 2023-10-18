from django import forms
from django.db import connection

from clinic.models import PatientInfo

class DateForm(forms.Form):
    def __init__(self, *args, device_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if device_id:
            available_dates = get_available_dates(device_id)
            choices = [(date, date) for date in available_dates]
            self.fields['date'] = forms.ChoiceField(choices=choices, widget=forms.Select)

def get_available_dates(device_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT date FROM daily_unlock WHERE device_id = %s", [device_id])
        rows = cursor.fetchall()
    return [row[0] for row in rows]

class WeekForm(forms.Form):
    def __init__(self, *args, device_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if device_id:
            available_weeks = get_available_weeks(device_id)
            choices = [(week, week) for week in available_weeks]
            self.fields['week_start_date'] = forms.ChoiceField(choices=choices, widget=forms.Select)

def get_available_weeks(device_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT week_start FROM weekly_unlocks WHERE device_id = %s", [device_id])
        rows = cursor.fetchall()
    return [row[0] for row in rows]

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientInfo
        fields = ['pa_name', 'age', 'sex', 'info', 'device_id']
        
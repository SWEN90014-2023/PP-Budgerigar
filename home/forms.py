from django import forms
from django.db import connection

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

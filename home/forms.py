from django import forms
from django.db import connection

def get_available_dates():
    with connection.cursor() as cursor:
        cursor.execute("SELECT date FROM daily_unlock")
        rows = cursor.fetchall()
    return [row[0] for row in rows]

class DateForm(forms.Form):
    date = forms.DateField(
        widget=forms.Select(choices=[(date, date) for date in get_available_dates()])
    )
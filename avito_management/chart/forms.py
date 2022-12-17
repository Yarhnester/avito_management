from django import forms
from .models import Chart


class DateChartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ('pvz', 'hours')

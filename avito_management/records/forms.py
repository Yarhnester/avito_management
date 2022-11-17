from django import forms
from .models import Record
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class RecordForm(forms.ModelForm):
    payment_date = forms.DateField(widget=DateInput())
    class Meta:
        model = Record
        # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
        fields = ('pvz', 'service', 'partner', 'contact', 'the_original_contract',
                  'rate', 'payment_date', 'document', 'edo', 'notes')

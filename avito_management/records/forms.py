from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
        fields = ('pvz', 'service', 'partner', 'contact', 'the_original_contract',
                  'rate', 'payment_date', 'document', 'edo', 'notes')

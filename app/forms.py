from django import forms
from .models import Vehicle
from django.core.exceptions import ValidationError

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['plate_number', 'driver_name', 'entry_weight', 'exit_weight']

    def clean_entry_weight(self):
        entry_weight = self.cleaned_data.get('entry_weight')
        if entry_weight is None or entry_weight <= 0:
            raise ValidationError('Invalid entry weight.')
        return entry_weight

    def clean_exit_weight(self):
        exit_weight = self.cleaned_data.get('exit_weight')
        if exit_weight is None or exit_weight <= 0:
            raise ValidationError('Invalid exit weight.')
        return exit_weight


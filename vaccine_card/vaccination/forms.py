from django import forms

from .models import Vaccine, Reinforcement


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['name', 'prevent_diseases']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),
            'prevent_diseases': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'style': 'resize: none; height: 100px',
                    'rows': '10',
                    'required': False
                }),
        }


class ReinforcementForm(forms.ModelForm):
    class Meta:
        model = Reinforcement
        fields = ['age', 'age_min', 'age_max']
        widgets = {
            'age_min': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),
            'age_max': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),
        }

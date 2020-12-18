from django import forms

from .models import Vaccine


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['name', 'age', 'age_min', 'age_max', 'prevent_diseases', 'reinforcement']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),
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
            'prevent_diseases': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'style': 'resize: none; height: 100px',
                    'rows': '10',
                    'required': False
            }),
            'reinforcement': forms.Select(
                attrs={
                    'required': False
                }
            )
        }

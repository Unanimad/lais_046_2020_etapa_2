from django import forms

from .models import HealthCenter, Address


class HealthCenterForm(forms.ModelForm):
    class Meta:
        model = HealthCenter
        fields = ['cnes', 'cnpj', 'name']
        widgets = {
            'cnes': forms.NumberInput(attrs={'class': 'form-control'}),
            'cnpj': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['cep', 'logradouro', 'numero', 'complemento', 'bairro', 'state', 'city']
        widgets = {
            'cep': forms.NumberInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
        }

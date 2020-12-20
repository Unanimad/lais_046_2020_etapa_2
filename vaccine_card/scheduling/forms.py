from django import forms

from vaccine_card.logistic.models import HealthCenter, VaccineStock
from vaccine_card.scheduling.models import Event


class EventForm(forms.ModelForm):
    # state = forms.ModelChoiceField(queryset=State.objects.all(), label='Estado')
    # city = forms.ModelChoiceField(queryset=City.objects.none(), label='Cidade')
    health_center = forms.ModelChoiceField(queryset=HealthCenter.objects.all(), label='Estabelecimento de Saúde')
    # vaccine = forms.ModelMultipleChoiceField(queryset=VaccineStock.objects.filter(stock__health_center__id=3),
    #                                          label='Vacinas')

    class Meta:
        model = Event
        fields = ['health_center', 'date', 'vaccine', 'note']
        widgets = {
            'date': forms.DateTimeInput(attrs={'id': 'date', 'class': 'form-control'}),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'resize: none; height: 100px',
                'rows': '10',
                'required': False
            }),
        }

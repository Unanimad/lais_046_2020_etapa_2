from django import forms

from vaccine_card.logistic.models import State, City, HealthCenter
from vaccine_card.scheduling.models import Event


class EventForm(forms.ModelForm):
    state = forms.ModelChoiceField(queryset=State.objects.all(), label='Estado')
    city = forms.ModelChoiceField(queryset=City.objects.none(), label='Cidade')
    health_center = forms.ModelChoiceField(queryset=HealthCenter.objects.none(), label='Estabelecimento de Saúde')

    class Meta:
        model = Event
        fields = ['state', 'city', 'health_center', 'date', 'vaccine', 'note']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'resize: none; height: 100px',
                'rows': '10',
                'required': False
            }),
        }

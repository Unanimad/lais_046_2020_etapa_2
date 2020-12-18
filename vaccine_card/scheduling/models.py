from django.db import models

from simple_history.models import HistoricalRecords

from vaccine_card.vaccination.models import Vaccine


class Event(models.Model):
    EVENT_STATUS = [
        ('E', 'Encaminhado'), ('R', 'Remarcado'), ('P', 'Aprovado'), ('D', 'Desistido')
    ]

    note = models.TextField(verbose_name='Observações')

    status = models.CharField(max_length=1, choices=EVENT_STATUS)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    vaccine = models.ManyToManyField(Vaccine, verbose_name=Vaccine._meta.verbose_name)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Evento'


class Vaccination(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, verbose_name='Agendamento')
    # professional = models.ForeignKey(Professional, on_delete=models.CASCADE, verbose_name='Profissional responsável')

    vaccines = models.ManyToManyField(Vaccine, verbose_name=Vaccine._meta.verbose_name)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'

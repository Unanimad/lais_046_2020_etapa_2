import os

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from simple_history.models import HistoricalRecords

from vaccine_card.logistic.models import HealthCenter
from vaccine_card.vaccination.models import Vaccine


class Event(models.Model):
    EVENT_STATUS = [
        ('E', 'Encaminhado'), ('R', 'Remarcado'), ('P', 'Aprovado'), ('D', 'Desistido'), ('C', 'Concluído')
    ]

    note = models.TextField(null=True, blank=True, verbose_name='Observações')

    status = models.CharField(max_length=1, default='E', choices=EVENT_STATUS)

    date = models.DateTimeField(verbose_name='Quando?')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    health_center = models.ForeignKey(HealthCenter, on_delete=models.CASCADE,
                                      verbose_name=HealthCenter._meta.verbose_name)
    vaccine = models.ManyToManyField(Vaccine, verbose_name=Vaccine._meta.verbose_name)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Evento'

    def __str__(self):
        return self.status

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        send_mail('Sua vacina está agendada!',
                  f'Você agendou vacina em {self.date} no {self.health_center} para {self.vaccine.all()}.',
                  settings.EMAIL_HOST_USER, os.environ.get('EMAIL_RECIPIENT').split(';'))


class Vaccination(models.Model):
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name='Agendamento')
    # professional = models.ForeignKey(Professional, on_delete=models.CASCADE, verbose_name='Profissional responsável')

    date = models.DateField(null=True, blank=True, verbose_name='Quando rebeceu a vacina?')

    vaccines = models.ManyToManyField(Vaccine, verbose_name=Vaccine._meta.verbose_name)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'

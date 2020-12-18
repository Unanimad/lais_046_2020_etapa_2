from django.db import models


from vaccine_card.vaccination.models import Vaccine


class Stock(models.Model):
    lot = models.PositiveSmallIntegerField(verbose_name='Lote')

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    vaccines = models.ManyToManyField(Vaccine, through='VaccineStock', verbose_name=Vaccine._meta.verbose_name)

    class Meta:
        verbose_name = 'Estoque'


class VaccineStock(models.Model):
    amount = models.PositiveSmallIntegerField(verbose_name='Quantidade recebida')
    remaining = models.PositiveSmallIntegerField(verbose_name='Quantidade restante')

    vaccine = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING, verbose_name=Vaccine._meta.verbose_name)
    stock = models.ForeignKey(Stock, on_delete=models.DO_NOTHING, verbose_name=Stock._meta.verbose_name)

    class Meta:
        verbose_name = 'Estoque de Vacina'

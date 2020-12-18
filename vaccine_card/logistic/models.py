from django.db import models

from vaccine_card.vaccination.models import Vaccine


class State(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nome')

    class Meta:
        verbose_name = 'Unidade Federativa'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=State._meta.verbose_name)

    class Meta:
        verbose_name = 'Município'

    def __str__(self):
        return self.name


class Address(models.Model):
    logradouro = models.CharField(max_length=150, verbose_name='Logradouro')
    numero = models.CharField(max_length=4, verbose_name='Número')
    complemento = models.CharField(max_length=50, null=True, blank=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=150, verbose_name='Bairro')
    cep = models.CharField(max_length=8, verbose_name='CEP')

    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=State._meta.verbose_name)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=City._meta.verbose_name)

    class Meta:
        verbose_name = 'Endereço'


class HealthCenter(models.Model):
    cnes = models.CharField(max_length=7, verbose_name='CNES')
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ')
    razao_social = models.CharField(max_length=255, verbose_name='Razão Social')

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    address = models.ManyToManyField(Address, verbose_name=Address._meta.verbose_name)

    class Meta:
        verbose_name = 'Estabelecimento de Saúde'
        verbose_name_plural = 'Estabelecimentos de Saúde'


class Stock(models.Model):
    lot = models.PositiveSmallIntegerField(verbose_name='Lote')

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    health_center = models.ForeignKey(HealthCenter, on_delete=models.CASCADE,
                                      verbose_name=HealthCenter._meta.verbose_name)

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

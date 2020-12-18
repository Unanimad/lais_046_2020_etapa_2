from django.db import models


class Vaccine(models.Model):
    AGE = [('D', 'Dia'), ('M', 'Mês'), ('Y', 'Ano')]

    name = models.CharField(max_length=50, verbose_name='Nome')
    age = models.CharField(max_length=1, choices=AGE, verbose_name='Idade em')
    age_min = models.CharField(max_length=3, verbose_name='Idade mínima')
    age_max = models.CharField(max_length=3, null=True, verbose_name='Idade máxima')
    prevent_diseases = models.TextField(verbose_name='Previne as doenças')

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    reinforcement = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Reforço')

    class Meta:
        verbose_name = 'Vacina'

    def __str__(self):
        return self.name

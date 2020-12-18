from django.db import models


class Vaccine(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    prevent_diseases = models.TextField(verbose_name='Previne as doenças')

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em:')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em:')

    reinforcement = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Reforço')

    class Meta:
        verbose_name = 'Vacina'

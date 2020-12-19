# Generated by Django 3.1.4 on 2020-12-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0002_auto_20201218_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccination',
            old_name='when',
            new_name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Quando?'),
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Quando?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('E', 'Encaminhado'), ('R', 'Remarcado'), ('P', 'Aprovado'), ('D', 'Desistido'), ('C', 'Concluído')], default='E', max_length=1),
        ),
        migrations.AlterField(
            model_name='historicalevent',
            name='status',
            field=models.CharField(choices=[('E', 'Encaminhado'), ('R', 'Remarcado'), ('P', 'Aprovado'), ('D', 'Desistido'), ('C', 'Concluído')], default='E', max_length=1),
        ),
    ]

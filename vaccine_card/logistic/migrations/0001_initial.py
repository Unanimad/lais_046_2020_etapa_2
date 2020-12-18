# Generated by Django 3.1.4 on 2020-12-18 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vaccination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.PositiveSmallIntegerField(verbose_name='Lote')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em:')),
            ],
            options={
                'verbose_name': 'Estoque',
            },
        ),
        migrations.CreateModel(
            name='VaccineStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Quantidade recebida')),
                ('remaining', models.PositiveSmallIntegerField(verbose_name='Quantidade restante')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistic.stock', verbose_name='Estoque')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vaccination.vaccine', verbose_name='Vacina')),
            ],
            options={
                'verbose_name': 'Estoque de Vacina',
            },
        ),
        migrations.AddField(
            model_name='stock',
            name='vaccines',
            field=models.ManyToManyField(through='logistic.VaccineStock', to='vaccination.Vaccine', verbose_name='Vacina'),
        ),
    ]
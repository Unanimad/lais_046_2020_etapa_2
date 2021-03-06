# Generated by Django 3.1.4 on 2020-12-18 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=4, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Endereço',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Município',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Unidade Federativa',
            },
        ),
        migrations.CreateModel(
            name='HealthCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnes', models.CharField(max_length=7, verbose_name='CNES')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('razao_social', models.CharField(max_length=255, verbose_name='Razão Social')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em:')),
                ('address', models.ManyToManyField(to='logistic.Address', verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Estabelecimento de Saúde',
                'verbose_name_plural': 'Estabelecimentos de Saúde',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistic.city', verbose_name='Município'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistic.state', verbose_name='Unidade Federativa'),
        ),
        migrations.AddField(
            model_name='stock',
            name='health_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='logistic.healthcenter', verbose_name='Estabelecimento de Saúde'),
            preserve_default=False,
        ),
    ]

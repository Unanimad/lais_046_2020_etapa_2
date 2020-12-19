# Generated by Django 3.1.4 on 2020-12-19 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0005_auto_20201218_2103'),
        ('scheduling', '0004_auto_20201219_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='health_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='logistic.healthcenter', verbose_name='Estabelecimento de Saúde'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='health_center',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='logistic.healthcenter', verbose_name='Estabelecimento de Saúde'),
        ),
    ]
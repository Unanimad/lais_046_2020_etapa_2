# Generated by Django 3.1.4 on 2020-12-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0003_auto_20201219_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name='Quando?'),
        ),
        migrations.AlterField(
            model_name='historicalevent',
            name='date',
            field=models.DateTimeField(verbose_name='Quando?'),
        ),
    ]

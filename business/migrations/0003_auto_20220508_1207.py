# Generated by Django 3.2 on 2022-05-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20220508_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='prix'),
        ),
        migrations.AlterField(
            model_name='formule',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='prix'),
        ),
        migrations.AlterField(
            model_name='surface',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='prix'),
        ),
    ]

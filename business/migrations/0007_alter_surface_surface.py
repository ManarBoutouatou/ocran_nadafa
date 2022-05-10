# Generated by Django 3.2 on 2022-05-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_alter_surface_surface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surface',
            name='surface',
            field=models.CharField(choices=[('S1', '70 - 200'), ('S2', '201 - 400'), ('S3', '401 - 600'), ('S4', '601 - 1000')], max_length=2, verbose_name='surface en m2'),
        ),
    ]

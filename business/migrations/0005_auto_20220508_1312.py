# Generated by Django 3.2 on 2022-05-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_formule_porte'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='surface',
            options={'verbose_name': 'surface', 'verbose_name_plural': 'surfaces'},
        ),
        migrations.AlterField(
            model_name='surface',
            name='surface',
            field=models.CharField(choices=[('S1', '70 - 200'), ('S1', '201 - 400'), ('S1', '201 - 400'), ('S1', '401 - 600'), ('S1', '601 - 1000')], max_length=2, verbose_name='surface en m2'),
        ),
    ]

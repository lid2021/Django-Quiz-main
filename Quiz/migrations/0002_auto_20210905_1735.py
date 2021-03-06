# Generated by Django 3.2.6 on 2021-09-05 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_auto_20210905_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='max_puntaje',
        ),
        migrations.RemoveField(
            model_name='quizusuario',
            name='fecha',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='puntaje_total',
            field=models.IntegerField(default=0, verbose_name='Puntaje Total'),
        ),
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='puntaje_obtenido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Puntaje Obtenido'),
        ),
        migrations.AlterField(
            model_name='quizusuario',
            name='puntaje_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Puntaje Total'),
        ),
    ]

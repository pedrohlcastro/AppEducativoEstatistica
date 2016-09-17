# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perguntas',
            name='correta',
            field=models.CharField(choices=[('1', 'Resposta 1'), ('2', 'Resposta 2'), ('3', 'Resposta 3'), ('4', 'Resposta 4')], default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='perguntas',
            name='name',
            field=models.CharField(choices=[('central', 'Central'), ('posicao', 'Posicao'), ('variancia', 'Variancia'), ('graficos', 'Graficos'), ('regressao', 'Regressao')], default='Nome', max_length=200),
        ),
        migrations.AddField(
            model_name='perguntas',
            name='number',
            field=models.CharField(default=1, max_length=3),
        ),
        migrations.AlterField(
            model_name='perguntas',
            name='link',
            field=models.CharField(default=2, max_length=3, verbose_name='Caso -1 vai para resultado'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0002_auto_20160916_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perguntas',
            name='pergunta',
            field=models.TextField(),
        ),
    ]
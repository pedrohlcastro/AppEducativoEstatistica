# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensino', '0007_ensino_linkvolta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ensino',
            name='linkVolta',
            field=models.CharField(default=2, max_length=3, verbose_name='Caso -1 vai para home'),
        ),
    ]

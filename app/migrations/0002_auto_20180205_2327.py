# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date of birth'),
        ),
    ]

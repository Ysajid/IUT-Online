# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20170428_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='university.Program'),
            preserve_default=False,
        ),
    ]
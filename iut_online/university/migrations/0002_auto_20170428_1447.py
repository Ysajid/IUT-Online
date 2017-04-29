# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_ptr',
        ),
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='university.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='permanent_address',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='present_address',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]

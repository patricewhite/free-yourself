# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-17 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170817_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='music/'),
        ),
    ]

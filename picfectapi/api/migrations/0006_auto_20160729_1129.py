# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160729_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnails',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20160729_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='original_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]

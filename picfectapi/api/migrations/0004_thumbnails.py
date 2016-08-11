# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_image_uploader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('effect', models.CharField(max_length=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('original_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Image')),
            ],
            options={
                'ordering': ['-date_modified'],
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-10-18 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images'),
        ),
    ]

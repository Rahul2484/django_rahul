# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151228_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.CharField(default='hi', max_length=200),
            preserve_default=False,
        ),
    ]

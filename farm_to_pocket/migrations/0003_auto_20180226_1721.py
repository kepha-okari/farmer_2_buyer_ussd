# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-26 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_to_pocket', '0002_auto_20180226_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Category', models.CharField(max_length=15)),
                ('NumberOfPages', models.IntegerField()),
            ],
        ),
    ]

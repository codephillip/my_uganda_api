# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161221_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
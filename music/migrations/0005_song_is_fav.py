# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-12 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-17 14:46
from __future__ import unicode_literals

import battle_platform.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(blank=True, null=True)),
                ('upload_game', models.IntegerField(choices=[(0, 'Royal war')], default=0)),
                ('upload_script', models.FileField(blank=True, upload_to=battle_platform.models.file_path_script)),
                ('replay', models.FileField(blank=True, upload_to=battle_platform.models.file_path_script)),
                ('upload_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

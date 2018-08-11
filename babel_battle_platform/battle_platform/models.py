# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

game_choices = ((0, 'Royal war'), (1, 'None'))


def file_path_script(instance, _):
    tt = str(instance.upload_time)
    return '%s.lua' % (tt.split('.')[0])


class UploadRecord(models.Model):
    upload_user = models.ForeignKey(User)
    upload_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    upload_game = models.IntegerField(choices=game_choices, default=0)
    upload_script = models.FileField(upload_to=file_path_script, blank=True)

# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import UploadRecord


class UploadRecordForm(ModelForm):
    class Meta:
        model = UploadRecord
        fields = ('upload_game', 'upload_script')
        widgets = {
            'upload_game': forms.RadioSelect(),
            'upload_script': forms.FileInput(attrs={'class': 'file_input'}),
        }
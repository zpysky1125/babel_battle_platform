# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import subprocess
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UploadRecordForm
from .models import UploadRecord
from django.conf import settings

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def homepage(request):
    if request.user.is_authenticated():
        upload_records = UploadRecord.objects.filter(upload_user=request.user)
        game_choices = {0: 'Royal war', 1: None}
        return render(request, 'homepage.html', {'username': request.user.username.split('@')[0],
                                                 'records': upload_records, 'choices': game_choices, })
    else:
        return render(request, 'homepage.html')


def login(request):
    information = {'option': 'login'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        information['username'] = username
        information['password'] = password
        if username == '':
            information['error'] = 'Email is required!'
        elif password == '':
            information['error'] = 'Password is required!'
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('battle:homepage'))
            else:
                information['error'] = 'Your email or password is wrong!'
    return render(request, 'login_register.html', information)


@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('battle:homepage'))


def register(request):
    information = {'option': 'register'}
    if request.method == 'POST':
        username = request.POST['r_username']
        password1 = request.POST['r_password1']
        password2 = request.POST['r_password2']
        information['r_username'] = username
        information['r_password1'] = password1
        information['r_password2'] = password2
        if username == '':
            information['r_error'] = 'Email is required!'
        elif password1 == '' or password2 == '':
            information['r_error'] = 'Password is required!'
        elif password1 != password2:
            information['r_error'] = 'Your passwords are not consistent!'
        else:
            if User.objects.filter(username=username).count() != 0:
                information['r_error'] = 'The email is already registered, please login!'
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                return HttpResponseRedirect(reverse('battle:homepage'))
    return render(request, 'login_register.html', information)


def run_script(file_id):
    script = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'check.py')
    subprocess.Popen(["python", script, file_id])


@login_required(login_url='/login/')
def script_upload(request):
    if request.method == 'POST':
        form = UploadRecordForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            script = model.upload_script
            script_split = str(script).split('.')
            if len(script_split) == 0 or script_split[-1] != 'lua':
                error = 'File format error!'
                return render(request, 'script_upload.html', {'form': form, 'error': error})
            else:
                model.upload_user = request.user
                model.save()
                origin_name = os.path.join(settings.MEDIA_ROOT, str(model.upload_time).split('.')[0].replace(' ', '_').replace(':', '')+ '.lua')
                new_name = os.path.join(settings.MEDIA_ROOT, str(model.id) + '.lua')
                os.rename(origin_name, new_name)
                model.upload_script.name = str(model.id) + '.lua'
                model.save()
                run_script(str(model.id))
                return HttpResponseRedirect(reverse('battle:homepage'))
    else:
        form = UploadRecordForm()
    return render(request, 'script_upload.html', {'form': form, })


@login_required(login_url='/login/')
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404


@login_required(login_url='/login/')
def video_play(request, video_id):
    static_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
    new_name = os.path.join(static_dir, 'video', video_id + '.mp4')
    if os.path.exists(new_name):
        return render(request, 'video_play.html', {'video_id': video_id})
    else:
        return HttpResponseRedirect(reverse('battle:homepage'))

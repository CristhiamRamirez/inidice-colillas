import os, logging
from django.contrib import messages
from typing import NewType
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.template.response import ContentNotRenderedError
from datetime import date, datetime, timedelta
from django.db.models.expressions import OrderBy
from django.http import HttpResponse
from django.utils import translation
from django.views import View
from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password

from django.db.models import Max, Sum

import rest_framework.exceptions

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=(logging.INFO))

def home(request):
    return render(request,'home.html')

def item(request):
    year = request.GET.get('year')
    name = request.GET.get('name')
    code = request.GET.get('code')
    period = models.Period.objects.filter(year=year, name=name)[0]
    boucher = models.Boucher.objects.filter(period=period, employee = code)[0]
    context = dict(
        package=boucher.package,
        index=boucher.index,
        key=boucher.key,
    )
    return render(request,'position.html',context=context)

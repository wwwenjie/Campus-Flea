# -*- coding: utf-8 -*-
# @Time    : 10/23/2019 7:57 PM
# @Author  : JIN Wenjie
# @FileName: user_views.py
# @Software: PyCharm
# @Blog    ：https://jinwenjie.me
from apps.user.models import User
from django.http import JsonResponse
import json


# Create your views here.
def detail(request):
    r = json.loads(request.body)
    return JsonResponse({})


def edit(request):
    r = json.loads(request.body)

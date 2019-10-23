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
def info(request):
    r = json.loads(request.body)
    uid = r['uid']
    u = User.objects.get(id=uid)
    return JsonResponse({
        'username': u.username,
        'email': u.email,
        'lastLogin': u.last_login,
        'avatar': u.avatar,
        'address': u.address,
        'sex': u.sex,
        'bday': u.bday,
        'bio': u.bio,
        'qq': u.qq,
        'wechat': u.wechat
    })


def edit(request):
    r = json.loads(request.body)

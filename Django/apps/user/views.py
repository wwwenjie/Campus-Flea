from datetime import datetime
from random import shuffle

from django.http import JsonResponse

# 导入数据库模型
from apps.user.models import User

# 异步发邮件
from celery_tasks.tasks import send_register_active_email

# 导入setting中的密文SECRET_KEY
from django.conf import settings

from django.core.cache import cache

# Json解析库
import json

# 阿里云核心SDK
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

# 正则
import re

# hash加密
import hashlib


# Create your views here.
def register(request):
    r = json.loads(request.body)
    account = r['account']
    password = r['password']
    code = r['code']
    if judge_type(account) is None:
        return JsonResponse({'success': False, 'msg': "账号格式有误！"})
    # 从redis缓存中读取缓存信息 account唯一
    check_code = cache.get(account)
    print(check_code)
    # 验证验证码是否正确
    if check_code == code:
        # 新加用户
        user = User()
        user.username = 'Sfleas_' + shuffle_str(True)[0:6]
        # 判断账号类型
        if judge_type(account) == 'phone':
            user.phone = account
        else:
            user.email = account
        # 密码加密
        user.password = encrypt(password)
        print(user.password)
        # 保存
        user.save()
        return JsonResponse({'success': True, 'msg': "注册成功！"})
    else:
        return JsonResponse({'success': False, 'msg': "验证码错误！"})


def send_verify(request):
    # 获取传过来的account
    r = json.loads(request.body)
    account = r['account']
    type = judge_type(account)
    if type is None:
        return JsonResponse({'success': False, 'msg': "账号格式有误！"})
    elif type == 'email':
        email = account
        # 判断该邮箱是否已经被注册
        try:
            if User.objects.get(email=email):
                return JsonResponse({'success': False, 'msg': "该邮箱已被注册！"})
        except User.DoesNotExist:
            pass

        # 生成验证码
        check_code = shuffle_str()[0:6]  # 截取0-6位
        # 异步发送邮件
        send_register_active_email.delay(email, check_code)

        # 缓存到redis 设置5分钟过期
        cache.set(email, check_code, 300)
        return JsonResponse({'success': True, 'msg': '发送成功！'})
    else:
        phone = account
        # 判断手机该是否已经被注册
        try:
            if User.objects.get(phone=phone):
                return JsonResponse({'success': False, 'msg': "该手机号已被注册！"})
        except User.DoesNotExist:
            pass

        # 生成验证码
        check_code = shuffle_str()[0:6]  # 截取0-6位

        # 发送短信
        resp = send_sms(phone, check_code)
        if resp == 'OK':
            # 缓存到redis 设置5分钟过期
            cache.set(phone, check_code, 300)
            return JsonResponse({'success': True, 'msg': '发送成功！'})
        else:
            return JsonResponse({'success': False, 'msg': resp})


def login(request):
    r = json.loads(request.body)
    account = r['account']
    password = r['password']
    # 获取数据
    try:
        if judge_type(account) == 'email':
            user = User.objects.get(email=account)
        else:
            user = User.objects.get(phone=account)
        # 验证密码
        print(encrypt(password))
        if encrypt(password) == user.password:
            # 重写token
            token = encrypt(user.id, str(datetime.now()))
            # 保存token
            user.user_token = token
            user.save()
            return JsonResponse({'uid': user.id, 'success': True, 'token': token})
        else:
            return JsonResponse({'success': False, 'msg': '账号或密码错误'})
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'msg': '账户不存在'})


def auth(request):
    r = json.loads(request.body)
    uid = r['uid']
    token = r['token']
    try:
        user = User.objects.get(id=uid)
        if user.user_token == token:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    except User.DoesNotExist:
        return JsonResponse({'success': False})


def shuffle_str(alphabet=None):
    # 验证码字库
    if alphabet:
        check_str = 'abcdefg0123456789'
    else:
        check_str = '0123456789'
    # 将字符串转换成列表
    str_list = list(check_str)
    # 调用random模块的shuffle函数打乱列表
    shuffle(str_list)
    # 将列表转字符串
    return ''.join(str_list)


# 加密
def encrypt(content, confusion=None):
    # 创建一个hash对象
    h = hashlib.sha256()
    # 提升密码复杂度，防止直接解密
    h.update(settings.SECRET_KEY.encode('utf-8'))
    # 填充要加密的数据
    h.update(str(content).encode('utf-8'))
    if confusion:
        h.update(str(confusion).encode('utf-8'))
    # 获取加密结果
    return h.hexdigest()


# 正则判断
def judge_type(account):
    phone = r"(^[1]([3-9])[0-9]{9}$)"
    email = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    try:
        if re.match(phone, account):
            return 'phone'
        else:
            return 'email' if re.match(email, account) else None
    # 前端直接传null时返回None
    except TypeError:
        return None


# 短信
def send_sms(phone, checkcode):
    client = AcsClient(settings.ACCESS_KEYID, settings.ACCESS_SECRET, 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "KingNetwork")
    request.add_query_param('TemplateCode', "SMS_174986857")
    request.add_query_param('TemplateParam', "{\"code\":\"%s\"}" % checkcode)

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))
    response = json.loads(response)
    return 'OK' if response['Message'] == "OK" else response['Message']

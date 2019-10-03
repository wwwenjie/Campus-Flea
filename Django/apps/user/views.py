
from datetime import datetime
from random import shuffle
# 导入View抽象类post,get方法
from django.views.generic import View

# 导入django自带的认证方法
from django.contrib.auth import authenticate
from django.http import JsonResponse

# 导入数据库模型
from apps.user.models import User  # 这李绝对路径会报错，我也不知道为啥，百度的

from celery_tasks.tasks import send_register_active_email
# 导入setting中的密文SECRET_KEY
from django.conf import settings

# 导入加密 需要 pip install itsdangerous
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# 解密时间过期异常类
from itsdangerous import SignatureExpired
# 导入setting中的密文SECRET_KEY
from django.conf import settings

from django.views.decorators.cache import cache_page
from django.core.cache import cache


# Create your views here.
class RegisterView(View):
    def get(self, request):
        pass

    def post(self, request):
        # username = request.POST.get('account')
        username = 'Sfleas_' + shuffle_str_username()[0:6]
        password = request.POST.get('password')
        email = request.POST.get('account')
        code = request.POST.get('code')
        print(password)
        print(email)
        print(code)
        # 判断验证码是否正确
        # print(request.session.get('checkcode'))
        # 从redis缓存中读取缓存信息 eamil唯一
        checkcode = cache.get(email)

        # 验证验证码是否正确
        if checkcode == code:
            # 3.业务逻辑处理
            # user = User.objects.create_user(username, email, password)
            #
            user = User()
            user.username = username
            user.email = email

            # 密码加密
            password = Encryption({'password': password})
            user.password = password
            # 保存
            user.save()
            return JsonResponse({'isSuccess': 'true', 'msg': "注册成功！"})
        else:
            return JsonResponse({'isSuccess': 'false', 'msg': "验证码错误！"})


class SendMailView(View):
    def get(self, request):
        pass

    def post(self, request):
        # 获取传过来的email
        email = request.POST.get('email')

        # 判断该邮箱是否已经被注册
        try:
            recheck = User.objects.get(email=email)
        except User.DoesNotExist:
            recheck = None

        # 假如邮箱已经存在
        if recheck:
            return JsonResponse({'isSuccess': 'false', 'msg': "该邮箱已被注册！"})

        # 生成验证码
        checkcodes = shuffle_str()[0:6]  # 截取0-6位

        # 异步发送邮件
        send_register_active_email.delay(email, checkcodes)

        # 缓存到redis 设置5分钟过期
        cache.set(email, checkcodes, 60)
        return JsonResponse({'isSuccess': "true", 'msg': '发送成功！'})


def shuffle_str():
    # 验证码字库
    checkstrs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # 将字符串转换成列表
    str_list = list(checkstrs)
    # 调用random模块的shuffle函数打乱列表
    shuffle(str_list)
    # 将列表转字符串
    return ''.join(str_list)


def shuffle_str_username():
    # 验证码字库
    checkstrs = 'abcdefg0123456789'
    # 将字符串转换成列表
    str_list = list(checkstrs)
    # 调用random模块的shuffle函数打乱列表
    shuffle(str_list)
    # 将列表转字符串
    return ''.join(str_list)


class LoginView(View):
    def get(self, request):
        pass

    def post(self, request):
        email = request.POST.get('account')
        password = request.POST.get('password')
        # 获取数据
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = ''

        if user:
            # 解密
            mysql_password = delEncryption(user.password)
            print(mysql_password['password'])
            if password == mysql_password['password']:
                # 加密文件
                info = {'id': user.id, 'datetimenow': str(datetime.now())}
                # 加密
                token = Encryption(info)
                #         保存token
                user.user_token = token
                user.save()
            return JsonResponse({'uid': user.id, 'isSuccess': 'true', 'token': token})
        else:
            return JsonResponse({'isSuccess': 'false', 'msg': '账户不存在'})


# 加密
def Encryption(info):
    # 生成token
    # 3600s为过期时间
    # setting.SECRET_KEY为密文
    serializer = Serializer(settings.SECRET_KEY)
    # 加密是dumps 解密为loads
    # 二进制形式
    token = serializer.dumps(info)  # bytes
    # 转化为utf-8形式
    token = token.decode()
    # 返回加密后的内容
    return token


# 解密
def delEncryption(val):
    # 创建对象
    serializer = Serializer(settings.SECRET_KEY)
    # 解密
    result = serializer.loads(val)
    # 返回结果
    return result

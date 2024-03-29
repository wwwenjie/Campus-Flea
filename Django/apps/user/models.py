from django.db import models
# 导入定义的基类
from db.base_model import BaseModel


# Create your models here.

class User(BaseModel):
    """用户模型类"""
    username = models.CharField(max_length=20, verbose_name='用户名称')
    email = models.EmailField(null=True, verbose_name='邮件')
    password = models.TextField(max_length=500, verbose_name='用户密码')
    last_login = models.DateTimeField(auto_now=True, verbose_name='最后登陆时间')
    avatar = models.URLField(null=True, verbose_name='头像')
    phone = models.CharField(max_length=20, null=True, verbose_name='电话')
    address = models.CharField(max_length=200, null=True, verbose_name='收货地址')
    user_token = models.TextField(max_length=500, null=True, verbose_name='用户token')
    # 杂项
    sex = models.CharField(max_length=5, null=True, verbose_name='性别')
    bday = models.DateTimeField(blank=True, null=True, verbose_name='生日')
    bio = models.CharField(max_length=50, null=True, verbose_name='简介')
    qq = models.CharField(max_length=30, null=True, verbose_name='QQ')
    wechat = models.CharField(max_length=30, null=True, verbose_name='微信')

    class Meta:
        db_table = 'SchoolFleasPro_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

from django.db import models
# 导入django自带的user抽象类
from django.contrib.auth.models import AbstractUser
# 导入定义的基类
from db.base_model import BaseModel


# Create your models here.

class User(AbstractUser, BaseModel, models.Model):
    """用户模型类"""
    user_token = models.CharField(max_length=200, verbose_name='用户token', null=True)

    class Meta:
        db_table = 'schoolfleas_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

from django.urls import path
from . import views, user_views

urlpatterns = [
    path('register', views.register),  # 用户注册
    path('register/verify', views.send_verify),  # 发送邮件
    path('login', views.login),  # 用户登录
    path('auth', views.auth),  # token验证
    path('user/detail', user_views.detail),  # 用户详情
    path('user/edit', user_views.edit),  # 用户编辑
]

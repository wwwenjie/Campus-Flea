from django.conf.urls import url
from apps.user.views import SendVerifyView, LoginView, RegisterView

urlpatterns = [
    url(r'^register$', RegisterView.as_view(), name='register'),  # 用户注册
    url(r'^register/verify$', SendVerifyView.as_view(), name='send_email'),  # 发送邮件
    url(r'^login$', LoginView.as_view(), name='login'),  # 用户登录
]

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/', include(('user.urls', 'user'), namespace='user')),  # 用户模块URL
    url(r'^goods/', include(('goods.urls', 'goods'), namespace='goods')),  # 商品模块URL
]

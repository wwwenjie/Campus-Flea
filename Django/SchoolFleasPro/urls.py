from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('user.urls', 'user'))),  # 用户模块URL
    path('goods/', include(('goods.urls', 'goods'))),  # 商品模块URL
    path('collect/', include(('collect.urls', 'collect')))  # 收藏购物URL
]

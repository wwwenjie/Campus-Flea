from django.urls import path
from . import views

urlpatterns = [
    path('browse', views.goods_browse),
    path('detail', views.goods_detail),
    path('search', views.goods_search),
    path('upload', views.goods_upload)
]

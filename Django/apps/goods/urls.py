from django.conf.urls import url
from apps.goods.views import GoodsMainView, GoodsUploadView, GoodsDetailView

urlpatterns = [
    url(r'^browse$', GoodsMainView.as_view(), name='goodsBrowse'),
    url(r'^upload$', GoodsUploadView.as_view(), name='goodsUpload'),
    url(r'^detail$', GoodsDetailView.as_view(), name='goodsDetail')
]

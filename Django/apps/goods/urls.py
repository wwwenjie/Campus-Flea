from django.conf.urls import url
from apps.goods.views import GoodsMainView

urlpatterns = [
    url(r'^goods/browse$', GoodsMainView.as_view(), name='goodsBrowse')
]

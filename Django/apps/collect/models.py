from django.db import models
from db.base_model import BaseModel

# Create your models here.
from apps.goods.models import Goods
from apps.user.models import User


class Collect(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户id', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name='商品id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'SchoolFleasPro_collect'
        verbose_name = '收藏表'
        verbose_name_plural = verbose_name


class ShopCart(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户id', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name='商品id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'SchoolFleasPro_cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

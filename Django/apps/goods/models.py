from decimal import Decimal
from django.db import models
from db.base_model import BaseModel


# Create your models here.

class Goods(BaseModel):
    """商品类模型"""
    STATUS_CHOICE = (
        (0, '下架'),
        (1, '上架'),
        (2, '待审核'),
    )
    status = models.IntegerField(default=0, choices=STATUS_CHOICE, verbose_name='商品状态')
    title = models.CharField(max_length=40, default='未获取到商品标题', verbose_name='商品标题')
    detail = models.TextField(default='该商品未留下详情', verbose_name='商品详情')
    category = models.CharField(max_length=20, default='其他', verbose_name='商品类型')
    url = models.TextField(null=True, verbose_name='商品图片链接')
    img_hash = models.TextField(null=True, verbose_name='商品图片hash')
    seller_id = models.IntegerField(verbose_name='卖家id')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name='商品价格')
    express = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name='商品运费')
    area = models.CharField(max_length=100, null=True, verbose_name='发货地')

    class Meta:
        db_table = 'SchoolFleasPro_goods'
        verbose_name = '商品表'
        verbose_name_plural = verbose_name


class RecommendGoods(BaseModel):
    goods_name = models.ForeignKey(Goods, verbose_name='商品id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'SchoolFleasPro_RecommendGoods'
        verbose_name = '推荐商品表'
        verbose_name_plural = verbose_name

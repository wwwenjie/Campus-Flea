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
    GOODS_TYPE = (
        ('book', '书籍'),
        ('newest', '最新'),
        ('daily', '生活用品'),
        ('3c', '3c数码'),
        ('dress', '鞋服美妆'),
        ('job', '兼职'),
        ('help', '求助')
    )
    goods_name = models.CharField(max_length=20, verbose_name='商品名称')
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    goods_images = models.ImageField(upload_to='goods', verbose_name='商品图片')
    goods_status = models.SmallIntegerField(default=0, choices=STATUS_CHOICE, verbose_name='商品状态')
    goods_type = models.CharField(max_length=10, choices=GOODS_TYPE, verbose_name='商品类型')

    class Meta:
        db_table = 'SchoolFleasPro_Goods'
        verbose_name = '商品表'
        verbose_name_plural = verbose_name


class RecommendGoods(BaseModel):
    goods_name = models.ForeignKey('Goods', verbose_name='商品名称', on_delete=models.CASCADE)

    class Meta:
        db_table = 'SchoolFleasPro_RecommendGoods'
        verbose_name = '推荐商品表'
        verbose_name_plural = verbose_name


class detailGoods(BaseModel):
    pass
    # thum
    # title
    # price
    # express
    # sellerName
    # sellerId
    # location
    # detail
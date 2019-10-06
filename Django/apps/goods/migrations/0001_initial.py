# Generated by Django 2.1.4 on 2019-10-06 17:08

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('status', models.IntegerField(choices=[(0, '下架'), (1, '上架'), (2, '待审核')], default=0, verbose_name='商品状态')),
                ('title', models.CharField(default='', max_length=40, verbose_name='商品标题')),
                ('detail', models.TextField(default='', verbose_name='商品详情')),
                ('category', models.CharField(default='', max_length=20, verbose_name='商品类型')),
                ('url', models.TextField(default='', verbose_name='商品图片链接')),
                ('img_hash', models.TextField(default='', verbose_name='商品图片hash')),
                ('seller_id', models.IntegerField(default='', verbose_name='卖家id')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, verbose_name='商品价格')),
                ('express', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, verbose_name='商品运费')),
                ('area', models.CharField(default='', max_length=20, verbose_name='发货地')),
            ],
            options={
                'verbose_name': '商品表',
                'verbose_name_plural': '商品表',
                'db_table': 'SchoolFleasPro_Goods',
            },
        ),
        migrations.CreateModel(
            name='RecommendGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('goods_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品名称')),
            ],
            options={
                'verbose_name': '推荐商品表',
                'verbose_name_plural': '推荐商品表',
                'db_table': 'SchoolFleasPro_RecommendGoods',
            },
        ),
    ]

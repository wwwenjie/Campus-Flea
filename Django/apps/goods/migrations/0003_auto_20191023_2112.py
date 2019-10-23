# Generated by Django 2.1.4 on 2019-10-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191018_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='area',
            field=models.CharField(max_length=20, null=True, verbose_name='发货地'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.CharField(default='其他', max_length=20, verbose_name='商品类型'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=models.TextField(default='该商品未留下详情', verbose_name='商品详情'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='img_hash',
            field=models.TextField(null=True, verbose_name='商品图片hash'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(default='未获取到商品标题', max_length=40, verbose_name='商品标题'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='url',
            field=models.TextField(null=True, verbose_name='商品图片链接'),
        ),
    ]

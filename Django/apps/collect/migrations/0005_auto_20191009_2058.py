# Generated by Django 2.1.4 on 2019-10-09 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0004_shopcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='user',
        ),
        migrations.DeleteModel(
            name='shopCart',
        ),
    ]
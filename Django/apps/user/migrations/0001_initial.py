# Generated by Django 2.1.4 on 2019-10-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('username', models.CharField(max_length=20, verbose_name='用户名称')),
                ('email', models.CharField(max_length=20, verbose_name='邮件')),
                ('password', models.CharField(max_length=500, verbose_name='用户密码')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='最后登陆时间')),
                ('headimg', models.ImageField(upload_to='user', verbose_name='头像')),
                ('phone', models.CharField(max_length=20, verbose_name='电话')),
                ('address', models.CharField(max_length=200, verbose_name='收货地址')),
                ('user_token', models.CharField(max_length=500, verbose_name='用户token')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'SchoolFleasPro_user',
            },
        ),
    ]

# Generated by Django 2.1.4 on 2019-10-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20191023_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='area',
            field=models.CharField(max_length=100, null=True, verbose_name='发货地'),
        ),
    ]

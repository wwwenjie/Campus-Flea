# Generated by Django 2.1.4 on 2019-10-09 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_collect_judgetype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='judgeType',
        ),
    ]

# Generated by Django 4.1 on 2023-02-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_rename_foreignid_comment_preid_comment_isreply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wxuser',
            name='avatarUrl',
            field=models.URLField(default='https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0', max_length=255),
        ),
    ]

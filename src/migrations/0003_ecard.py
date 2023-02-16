# Generated by Django 4.1 on 2023-02-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_alter_notice_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ecard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ownerid', models.IntegerField(unique=True)),
                ('imgpath', models.CharField(max_length=255)),
            ],
        ),
    ]

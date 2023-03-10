# Generated by Django 3.2.8 on 2023-02-13 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='career',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('unit', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'career',
            },
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-16 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='imageURL',
            field=models.CharField(default=datetime.time, max_length=255),
            preserve_default=False,
        ),
    ]

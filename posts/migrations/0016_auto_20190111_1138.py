# Generated by Django 2.0 on 2019-01-11 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20181206_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='corner',
            name='video',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.URLField(default=''),
        ),
    ]

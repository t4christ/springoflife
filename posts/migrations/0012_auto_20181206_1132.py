# Generated by Django 2.0 on 2018-12-06 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20181205_1559'),
    ]

    operations = [

        migrations.AddField(
            model_name='messaging',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
     
    ]
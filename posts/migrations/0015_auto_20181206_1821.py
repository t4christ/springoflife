# Generated by Django 2.0 on 2018-12-06 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20181206_1758'),
    ]

    operations = [
    
        migrations.AlterField(
            model_name='corner',
            name='corner',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    
    ]

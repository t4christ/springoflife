# Generated by Django 2.0 on 2019-10-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol', '0010_auto_20191009_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praywithus',
            name='Date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
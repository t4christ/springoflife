# Generated by Django 2.0 on 2019-10-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol', '0007_auto_20191005_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='growmission',
            name='image',
        ),
        migrations.RemoveField(
            model_name='growmission',
            name='village',
        ),
        migrations.AddField(
            model_name='growmission',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]

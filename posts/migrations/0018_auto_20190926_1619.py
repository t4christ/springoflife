# Generated by Django 2.2.5 on 2019-09-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20190215_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_image',
            field=models.ImageField(blank=True, height_field='height_field', max_length=10000, null=True, upload_to='https://None.s3.amazonaws.com/media/', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', max_length=10000, null=True, upload_to='https://None.s3.amazonaws.com/media/', width_field='width_field'),
        ),
    ]
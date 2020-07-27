# Generated by Django 2.2.5 on 2019-09-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20190926_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='describe_one',
        ),
        migrations.AddField(
            model_name='post',
            name='describe_two',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_image',
            field=models.ImageField(blank=True, height_field='height_field', max_length=10000, null=True, upload_to='posts', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', max_length=10000, null=True, upload_to='posts', width_field='width_field'),
        ),
    ]

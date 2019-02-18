# Generated by Django 2.0 on 2018-12-05 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Corner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corner', models.CharField(default='', max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500, unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', max_length=10000, null=True, upload_to='posts', width_field='width_field')),
                ('content_image', models.ImageField(blank=True, height_field='height_field', max_length=10000, null=True, upload_to='posts', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('read_time', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='CornerList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('tag_name', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Messaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=500)),
                ('message', models.TextField(default='')),
                ('sender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500, unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', max_length=10000, null=True, upload_to='posts', width_field='width_field')),
                ('content_image', models.ImageField(blank=True, height_field='height_field', max_length=10000, null=True, upload_to='posts', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('read_time', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]

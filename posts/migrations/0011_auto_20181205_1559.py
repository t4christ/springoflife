# Generated by Django 2.0 on 2018-12-05 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):



    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0010_cornerlist'),
    ]


    operations = [
        migrations.CreateModel(
            name='Messaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=500)),
                ('message', models.TextField(default='')),
                ('sender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='corner',
            name='corner',
            field=models.CharField(default='', max_length=100),
        ),
        
    ]
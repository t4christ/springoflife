# Generated by Django 2.0 on 2018-10-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_myuser_stat_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_partner',
            field=models.BooleanField(default=False),
        ),
    ]

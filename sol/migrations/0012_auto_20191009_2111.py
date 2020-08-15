# Generated by Django 2.0 on 2019-10-09 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sol', '0011_auto_20191009_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayerpoint',
            name='pray_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pray_time', to='sol.PrayWithUs'),
        ),
        migrations.AlterField(
            model_name='praywithus',
            name='Date',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
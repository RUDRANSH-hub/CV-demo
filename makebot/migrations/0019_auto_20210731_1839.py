# Generated by Django 3.2 on 2021-07-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makebot', '0018_auto_20210729_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='acherviment1',
            field=models.TextField(default='', max_length=1000, verbose_name='acherviment1'),
        ),
        migrations.AddField(
            model_name='profile',
            name='previous_workr',
            field=models.CharField(default='', max_length=500, verbose_name='previous_work'),
        ),
    ]

# Generated by Django 3.2 on 2021-07-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makebot', '0014_auto_20210729_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='web',
            field=models.TextField(default='', max_length=1000, verbose_name='web'),
        ),
    ]

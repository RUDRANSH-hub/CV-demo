# Generated by Django 3.2 on 2021-07-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makebot', '0015_profile_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.CharField(default='', max_length=10, verbose_name='number'),
        ),
    ]

# Generated by Django 3.2 on 2021-07-28 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makebot', '0005_alter_profile_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='DOB',
        ),
    ]

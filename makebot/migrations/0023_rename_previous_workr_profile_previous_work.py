# Generated by Django 3.2 on 2021-07-31 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makebot', '0022_profile_coding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='previous_workr',
            new_name='previous_work',
        ),
    ]
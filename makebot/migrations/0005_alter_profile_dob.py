# Generated by Django 3.2 on 2021-07-28 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makebot', '0004_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]

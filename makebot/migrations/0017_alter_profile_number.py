# Generated by Django 3.2 on 2021-07-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makebot', '0016_profile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(max_length=10, verbose_name='number'),
        ),
    ]

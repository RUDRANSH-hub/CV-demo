# Generated by Django 3.2 on 2021-07-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=254)),
            ],
        ),
    ]

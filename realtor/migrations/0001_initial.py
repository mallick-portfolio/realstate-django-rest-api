# Generated by Django 4.1.3 on 2022-12-20 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biodata', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('image', models.ImageField(upload_to='realtor')),
                ('top_seller', models.BooleanField(default=False)),
                ('date_hired', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-16 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField()),
                ('Date_Time', models.DateTimeField(default=datetime.datetime(2024, 11, 16, 6, 28, 13, 99452))),
            ],
        ),
    ]

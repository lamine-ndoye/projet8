# Generated by Django 4.2.2 on 2023-06-20 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='auteur',
        ),
        migrations.AlterField(
            model_name='article',
            name='pulish',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 20, 13, 10, 42, 968146, tzinfo=datetime.timezone.utc)),
        ),
    ]
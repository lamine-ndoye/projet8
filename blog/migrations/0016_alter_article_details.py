# Generated by Django 4.2.4 on 2023-08-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_article_description_alter_article_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='details',
            field=models.CharField(),
        ),
    ]
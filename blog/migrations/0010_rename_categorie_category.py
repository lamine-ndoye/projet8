# Generated by Django 4.2.3 on 2023-07-18 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_categorie_alter_article_publish'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Category',
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-25 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20181124_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strain',
            old_name='fav',
            new_name='cbd',
        ),
        migrations.RenameField(
            model_name='strain',
            old_name='deal',
            new_name='favorite',
        ),
    ]
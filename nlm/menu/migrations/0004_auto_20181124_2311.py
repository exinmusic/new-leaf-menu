# Generated by Django 2.1.3 on 2018-11-24 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20181124_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='deal',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strain',
            name='fav',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

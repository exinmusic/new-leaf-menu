# Generated by Django 2.1.3 on 2018-11-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20181124_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strain',
            name='cbd',
        ),
        migrations.RemoveField(
            model_name='strain',
            name='thc',
        ),
        migrations.AddField(
            model_name='strain',
            name='pheno',
            field=models.CharField(default='hybrid', max_length=15),
            preserve_default=False,
        ),
    ]

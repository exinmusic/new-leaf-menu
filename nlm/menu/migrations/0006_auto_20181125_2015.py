# Generated by Django 2.1.3 on 2018-11-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20181125_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strain',
            name='pheno',
            field=models.CharField(choices=[('sativa', 'Sativa'), ('hybrid', 'Hybrid'), ('indica', 'Indica')], max_length=6),
        ),
    ]

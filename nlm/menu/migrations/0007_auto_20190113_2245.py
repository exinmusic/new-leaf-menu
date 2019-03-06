# Generated by Django 2.1.3 on 2019-01-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20181125_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advanced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensary', models.CharField(max_length=140)),
                ('leafly', models.CharField(max_length=140)),
            ],
        ),
        migrations.AlterField(
            model_name='strain',
            name='cbd',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='strain',
            name='favorite',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='strain',
            name='pheno',
            field=models.CharField(choices=[('sativa', 'Sativa'), ('hybrid', 'Hybrid'), ('indica', 'Indica')], default='hybrid', max_length=6),
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0007_auto_20190808_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='gpa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]

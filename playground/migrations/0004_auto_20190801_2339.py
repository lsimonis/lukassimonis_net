# Generated by Django 2.1.7 on 2019-08-01 23:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='startdate',
        ),
        migrations.AddField(
            model_name='experience',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
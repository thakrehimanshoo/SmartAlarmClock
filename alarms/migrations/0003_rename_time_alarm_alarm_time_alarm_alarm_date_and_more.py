# Generated by Django 4.2.3 on 2024-11-12 11:39

import django
from django.utils import timezone
from django.db import migrations, models
import django.utils.timezone as timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alarms', '0002_remove_alarm_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarm',
            old_name='time',
            new_name='alarm_time',
        ),
        migrations.AddField(
            model_name='alarm',
            name='alarm_date',
            field = django.db.models.DateField(default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alarm',
            name='text',
            field=models.CharField(default='Alarm', max_length=200),
            preserve_default=False,
        ),
    ]

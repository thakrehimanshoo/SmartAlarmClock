# Generated by Django 4.2.3 on 2024-11-12 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='message',
        ),
    ]

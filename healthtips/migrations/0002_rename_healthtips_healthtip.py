# Generated by Django 4.1.11 on 2024-10-02 18:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('healthtips', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HealthTips',
            new_name='HealthTip',
        ),
    ]

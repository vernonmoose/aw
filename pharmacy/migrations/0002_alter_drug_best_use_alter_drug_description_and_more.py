# Generated by Django 4.1.11 on 2024-10-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='best_use',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='drug',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='drug',
            name='instructions',
            field=models.TextField(max_length=1500),
        ),
    ]

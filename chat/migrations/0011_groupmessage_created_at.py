# Generated by Django 5.0.3 on 2024-03-13 10:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_auto_20240306_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-18 11:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0018_delete_userrecommendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendationviews',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

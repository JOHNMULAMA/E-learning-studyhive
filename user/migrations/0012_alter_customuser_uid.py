# Generated by Django 5.0.3 on 2024-03-20 11:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_customuser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=50, unique=True),
        ),
    ]

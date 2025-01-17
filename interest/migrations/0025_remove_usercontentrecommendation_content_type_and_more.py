# Generated by Django 5.0.3 on 2024-04-03 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0024_remove_usercontentrecommendation_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontentrecommendation',
            name='content_type',
        ),
        migrations.AddField(
            model_name='usercontentrecommendation',
            name='user_content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_content_recommendation', to='interest.usercontent'),
            preserve_default=False,
        ),
    ]

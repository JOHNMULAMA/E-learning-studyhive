# Generated by Django 3.2.24 on 2024-03-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_groupmessage_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='on_call',
            field=models.BooleanField(default=False),
        ),
    ]
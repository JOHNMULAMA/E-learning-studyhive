# Generated by Django 5.0 on 2024-01-01 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_connection'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReportedUsers',
            new_name='ReportedUser',
        ),
    ]

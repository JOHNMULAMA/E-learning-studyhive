# Generated by Django 3.2.24 on 2024-02-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='admin',
        ),
        migrations.AddField(
            model_name='groupmember',
            name='allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='groupmember',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('member', 'member')], default='member', max_length=10),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]

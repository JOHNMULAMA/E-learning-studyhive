# Generated by Django 5.0.3 on 2024-04-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0023_usercontentrecommendation_uid_alter_category_uid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontentrecommendation',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='usercontentrecommendation',
            name='user_content',
        ),
        migrations.AddField(
            model_name='usercontent',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='user_content/thumbnail/'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_communityfile_communitylike'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='community_post_status',
            field=models.BooleanField(default=True),
        ),
    ]

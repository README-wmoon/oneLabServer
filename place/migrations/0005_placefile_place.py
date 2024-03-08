# Generated by Django 5.0.2 on 2024-03-05 16:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

from place.models import PlaceFile


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_remove_placefile_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='placefile',
            name='place',
            field=models.ForeignKey(PlaceFile, default=1, on_delete=django.db.models.deletion.PROTECT),
            preserve_default=False,
        ),
    ]
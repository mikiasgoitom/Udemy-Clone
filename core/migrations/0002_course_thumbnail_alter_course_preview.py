# Generated by Django 5.0.6 on 2024-06-03 13:25

import core.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=core.models.get_course_thumbnail_file_path, validators=[django.core.validators.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.FileField(upload_to=core.models.get_course_preview_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'webm'])]),
        ),
    ]

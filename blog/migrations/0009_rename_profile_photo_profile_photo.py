# Generated by Django 5.1.4 on 2024-12-31 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_profile_picture_profile_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='photo',
        ),
    ]
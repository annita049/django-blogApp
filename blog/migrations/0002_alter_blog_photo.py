# Generated by Django 5.1.4 on 2024-12-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, default='photos/pexels-no_photo.jpg', null=True, upload_to='photos/'),
        ),
    ]

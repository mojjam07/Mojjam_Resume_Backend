# Generated by Django 5.1 on 2024-09-16 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_images_newtestimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtestimonial',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='new_testimonial_pics/'),
        ),
    ]

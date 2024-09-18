# Generated by Django 5.1 on 2024-09-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('service_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

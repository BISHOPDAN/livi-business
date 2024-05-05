# Generated by Django 5.0.3 on 2024-04-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0024_hremployees_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyservices',
            name='service_cover_picture',
        ),
        migrations.AddField(
            model_name='companyservices',
            name='available_country',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='companyservices',
            name='available_state',
            field=models.CharField(default='', max_length=20),
        ),
    ]

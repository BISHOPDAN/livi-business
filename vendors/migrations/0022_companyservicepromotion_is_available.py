# Generated by Django 5.0.3 on 2024-04-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0021_companyenquiry_enquiry_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyservicepromotion',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]

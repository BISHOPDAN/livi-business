# Generated by Django 5.0.3 on 2024-04-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='company_url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
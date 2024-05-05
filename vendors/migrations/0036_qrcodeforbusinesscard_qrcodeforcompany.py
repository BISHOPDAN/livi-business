# Generated by Django 5.0.3 on 2024-04-25 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0035_remove_businesscards_designation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QrCodeForBusinessCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_image', models.ImageField(upload_to='business_card_qr_image')),
                ('url', models.CharField(max_length=255)),
                ('business_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.businesscards')),
            ],
        ),
        migrations.CreateModel(
            name='QrCodeForCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_image', models.ImageField(upload_to='company_qr_image')),
                ('url', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.companyprofile')),
            ],
        ),
    ]
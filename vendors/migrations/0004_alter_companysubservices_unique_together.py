# Generated by Django 5.0.3 on 2024-04-06 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_remove_companyservices_discount_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='companysubservices',
            unique_together={('company_services', 'sub_service_name')},
        ),
    ]
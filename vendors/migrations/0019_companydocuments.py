# Generated by Django 5.0.3 on 2024-04-15 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0018_companyservicepromotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=30)),
                ('issued_date', models.DateField()),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('document', models.FileField(upload_to='company_documents')),
                ('is_available', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.companyprofile')),
            ],
        ),
    ]

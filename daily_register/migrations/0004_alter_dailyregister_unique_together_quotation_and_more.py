# Generated by Django 5.0.3 on 2024-04-16 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_register', '0003_dailyregister'),
        ('vendors', '0020_alter_companydocuments_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dailyregister',
            unique_together={('company', 'order_id')},
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_identifier', models.CharField(db_index=True, max_length=10)),
                ('payment_terms', models.TextField()),
                ('requirements', models.TextField()),
                ('pricing', models.TextField()),
                ('other_terms', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
                ('quotation_date', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.companyprofile')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_register.customer')),
            ],
        ),
        migrations.CreateModel(
            name='QuotationItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=1)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('vat_or_tax', models.CharField(blank=True, max_length=30, null=True)),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_register.quotation')),
            ],
        ),
    ]

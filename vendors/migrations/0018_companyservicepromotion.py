# Generated by Django 5.0.3 on 2024-04-14 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0017_hremployees_payroll_delete_hrsystememployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyServicePromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_name', models.CharField(max_length=100)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('promotion_valid_from', models.DateField()),
                ('promotion_valid_to', models.DateField()),
                ('promotion_cover_picture', models.ImageField(blank=True, upload_to='company_promotion_picture')),
                ('voucher_code', models.CharField(max_length=100)),
                ('one_time_usage', models.BooleanField(default=False)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.companyprofile')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.companyservices')),
                ('sub_service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.companysubservices')),
            ],
            options={
                'unique_together': {('company_id', 'service_id', 'sub_service_id', 'promotion_name')},
            },
        ),
    ]

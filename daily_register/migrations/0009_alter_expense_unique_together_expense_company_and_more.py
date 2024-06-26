# Generated by Django 5.0.3 on 2024-04-16 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_register', '0008_statementofaccounts_expense_paymentcollections'),
        ('vendors', '0020_alter_companydocuments_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='expense',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='expense',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vendors.companyprofile'),
        ),
        migrations.AlterUniqueTogether(
            name='expense',
            unique_together={('to', 'description', 'amount_paid', 'company', 'payment_type', 'expense_against')},
        ),
    ]

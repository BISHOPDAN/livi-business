# Generated by Django 5.0.3 on 2024-04-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_register', '0005_quotation_quotation_status'),
        ('vendors', '0020_alter_companydocuments_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterUniqueTogether(
            name='quotation',
            unique_together={('company', 'quotation_identifier')},
        ),
        migrations.AlterUniqueTogether(
            name='quotationitems',
            unique_together={('quotation', 'description')},
        ),
    ]

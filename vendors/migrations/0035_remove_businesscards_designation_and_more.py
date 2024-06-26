# Generated by Django 5.0.3 on 2024-04-25 22:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0034_remove_leadgeneration_domain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesscards',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='businesscards',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='businesscards',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='businesscards',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='businesscards',
            name='hr_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.hremployees'),
        ),
    ]

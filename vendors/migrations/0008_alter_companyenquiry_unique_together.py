# Generated by Django 5.0.3 on 2024-04-08 10:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0007_alter_companyenquiry_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='companyenquiry',
            unique_together={('user', 'sub_service', 'email', 'message')},
        ),
    ]

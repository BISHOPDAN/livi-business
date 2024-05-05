from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from decouple import config
import tempfile
from django.core.files.base import ContentFile
from vendors.models import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from vendors.views import create_qr_code
channel_layer = get_channel_layer()
domain = config('front_end_url')


@receiver(post_save, sender=CompanyProfile)
def create_vendor_verify_notification(sender, instance, created, **kwargs):
    if created:
        VendorNotification.objects.create(
            company=instance,
            text=f"Verify request from {instance.company_name} company",
        )
        notification_text = f"New company {instance.company_name} registered just now pleas verify the details!!"
        async_to_sync(channel_layer.group_send)(
            "admin_group",
            {
                'type': 'create_notification',
                'message': notification_text
            }
        )


@receiver(post_save, sender=CompanyProfile)
def create_qr_code_for_company(sender, instance, created, **kwargs):
    if created:
        company_url = f"{domain}{instance.tagline}/"
        qr_img = create_qr_code(company_url)
        img_temp = tempfile.NamedTemporaryFile(delete=True)
        qr_img.save(img_temp, format='PNG')
        img_temp.seek(0)
        qr_image_file = ContentFile(img_temp.read())
        qr_code = QrCodeForCompany(
            company=instance,
            url=company_url
        )
        qr_code.qr_image.save(f'{instance.company_name}_qr.png', qr_image_file)
        qr_code.save()

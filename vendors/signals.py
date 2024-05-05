import tempfile
from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from decouple import config
from .models import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .views import create_qr_code
channel_layer = get_channel_layer()

domain = config('front_end_url')


@receiver(post_save, sender=HREmployees)
def create_business_card(sender, instance, created, **kwargs):
    check_confirmation = False
    if created:
        if instance.business_card_confirmation:
            check_confirmation = True
        else:
            check_confirmation = False
        BusinessCards.objects.create(
            company=instance.company,
            hr_employee=instance,
            is_available=check_confirmation
        )


@receiver(post_save, sender=BusinessCards)
def create_qr_code_for_business_card(sender, instance, created, **kwargs):
    if created:
        card_url = f"{domain}cardview/?email={instance.hr_employee.email}"
        qr_img = create_qr_code(card_url)
        img_temp = tempfile.NamedTemporaryFile(delete=True)
        qr_img.save(img_temp, format='PNG')
        img_temp.seek(0)
        qr_image_file = ContentFile(img_temp.read())
        qr_code = QrCodeForBusinessCard(
            business_card=instance,
            url=card_url
        )
        qr_code.qr_image.save(f'{instance.id}_qr.png', qr_image_file)
        qr_code.save()


@receiver(post_save, sender=HREmployees)
def create_business_card_after_update(sender, instance, created, **kwargs):
    if not created:
        check_confirmation = False
        if instance.business_card_confirmation:
            check_confirmation = True
        else:
            check_confirmation = False
        card_detail = BusinessCards.objects.get(hr_employee=instance.id)
        card_detail.is_available = check_confirmation
        card_detail.save()

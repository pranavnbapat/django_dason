from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.models import UserActivityLog
import logging

logger = logging.getLogger('backend.models')


@receiver(post_save, sender=UserActivityLog)
def log_user_activity(sender, instance, created, **kwargs):
    if created:
        log_entry = f"{instance.user} - {instance.activity} - {instance.timestamp}"
        logger.info(log_entry)

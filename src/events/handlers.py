from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from .models import Event
from .signals import event_did_trigger


@receiver(event_did_trigger)
def handle_post_save_signal(
    sender,
    event_type,
    content_object,
    user=None,
    *args,
    **kwargs
    ):
    # print(sender, event_type, content_object, user)
    Event.objects.create(
        type=event_type,
        content_object=content_object,
        user=user,
        time=timezone.now()
    )
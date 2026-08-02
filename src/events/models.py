from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from timescale.db.models.models import TimescaleModel
# from contacts.models import Contact



User = settings.AUTH_USER_MODEL

# time series
class Event(TimescaleModel):
    class EventType(models.TextChoices):
        UNKNOWN = "unknown", "Unknown event type"
        CREATED = "created", "Create Event"
        SYNC = "sync", "Sync Event"
        VIEWED = "viewed", "View Event"
        SAVED = "saved", "Saved or Update Event"

    user = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        help_text="Performed by user", 
        related_name="myevents")
    type = models.CharField(
        max_length=40, 
        default=EventType.VIEWED, 
        choices=EventType.choices)
    object_id = models.PositiveBigIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    #timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"])
        ]
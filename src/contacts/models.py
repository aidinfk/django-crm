from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from events.models import Event
from django.db import models



User = settings.AUTH_USER_MODEL


class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mycontacts"
    )
    email = models.EmailField(db_index=True)
    first_name = models.CharField(max_length=120, default="", blank=True)
    last_name = models.CharField(max_length=120, default="", blank=True)
    notes = models.TextField(blank=True, default="")
    last_edited_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="my_contact_edits"
    )
    last_sync = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    events = GenericRelation(Event)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return f"/contacts/{self.id}/"
    

import uuid

from django.db import models


class Text(models.Model):
    """text message"""

    SHIRT_PROVIDER = (
        ("plug", "provider Plug"),
        ("file", "provider File"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=140, blank=True, default="")
    phone_number = models.CharField(max_length=12)
    sent = models.BooleanField(
        default=False, help_text="has the message been sent successfully"
    )
    delivered = models.BooleanField(
        default=False, help_text="has the message been delivered successfully"
    )
    provider = models.CharField(
        max_length=20, default="plug", blank=True, choices=SHIRT_PROVIDER
    )
    date_created = models.DateTimeField(
        auto_created=True, help_text="YYYY-MM-DDThh:mm<TZDSuffix>"
    )

    def __str__(self):
        return self.body

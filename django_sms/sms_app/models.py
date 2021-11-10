import uuid

from django import forms
from django.db import models


def validators_number_phone(value):
    if not value.isdigit():
        raise forms.ValidationError("Номер телефона должен состоять только из цифр")


class Text(models.Model):
    """Model representing a text message"""

    SHIRT_PROVIDER = (
        ("plug", "provider Plug"),
        ("file", "provider File"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=140, blank=True, default="")
    phone_number = models.CharField(max_length=12, validators=[validators_number_phone])
    delivered = models.CharField(max_length=10, default="unknown")
    provider = models.CharField(
        max_length=20, default="plug", blank=True, choices=SHIRT_PROVIDER
    )
    date_created = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.body=} {self.phone_number=} {self.provider=} \n"
            f"{self.id=} {self.delivered=}"
        )

# from multiprocessing import Queue, Process

from .models import Text
from .strategy import Context, FileProvider, PlugProvider


def send(payload):
    """
    Sets the number of attempts to send.
    When attempts are exhausted or the message is sent.
    Fills in the delivered field in the database
    """
    if not ("amount_send" in payload):
        make_send(payload)
    elif payload["delivered"] != "sent" and payload["amount_send"] > 0:
        make_send(payload)
    else:
        entries = Text.objects.get(id=payload["id"])
        entries.delivered = payload["delivered"]
        entries.save()


def make_send(payload):
    """
    depending on the selected operator determines the method of sending the message
    """
    provider = payload["provider"]
    if provider == "plug" or provider == "":
        if not ("amount_send" in payload):
            payload.update({"delivered": "unknown", "amount_send": 1})
        context = Context(PlugProvider(payload))
        payload = context.send_sms()
    elif provider == "file":
        if not ("amount_send" in payload):
            payload.update({"delivered": "unknown", "amount_send": 3})
        context = Context(FileProvider(payload))
        payload = context.send_sms()
    send(payload)

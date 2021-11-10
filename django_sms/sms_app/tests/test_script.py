# from ..models import Text
# from ..script import send, make_send
#
#
# payload = {
#     'id': '827a6275-2859-4fb8-9bb0-0432e5409ceb',
#     'body': 'Hi Pasha',
#     'phone_number': '89743674648',
#     'provider': 'file'
#     }
#
#
# def test_send_send():
#     """checks that the message has been sent"""
#     send(payload)
#     entries = Text.objects.get(id=payload['id'])
#     delivered = entries.delivered
#     assert delivered == 'sent'
#
#
# def test_send_not_send():
#     """checks that the message has not been sent"""
#
#
# def test_send_uncnown():
#     """checks that the information about sending the message is not available"""

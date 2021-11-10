# from django.test import TestCase
# from ..models import Text
#
#
# class TestModelTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         Text.objects.create(body='Hi Pasha', phone_number='89743674648', provider='file')
#
#     def test_body_max_length(self):
#         text = Text.objects.get(id=1)
#         max_length = text._meta.get_field('body').max_length
#         self.assertEquals(max_length, 140)

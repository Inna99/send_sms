# from django.shortcuts import render
# from rest_framework.decorators import api_view, parser_classes
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Text
from .serializers import TextSerializer

# from rest_framework.parsers import JSONParser
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# # from django_sms.sms_app.script import some_func
# from rest_framework.views import APIView


# class ListTextAPIView(APIView):
#     # permission_classes = (IsAuthenticated,)
#     serializer_class = TextSerializer
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.provider for user in Text.objects.all()]
#         return Response(usernames)


class ListTextAPIView(ListAPIView):
    """This endpoint list all of the available texts from the database"""

    # permission_classes = (IsAuthenticated,)
    queryset = Text.objects.all()
    serializer_class = TextSerializer


class CreateTextAPIView(CreateAPIView):
    """This endpoint allows for creation of a text"""

    # permission_classes = (IsAuthenticated,)
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def post(self, request, *args, **kwargs):
        """
        сохраняем результат работы функции в бд Text.
        some_func(request.data)
        """
        return self.create(request, *args, **kwargs)

    # parser_classes = [JSONParser]

    # def post(self, request, format=None):
    #     return Response({'received data': request.data})

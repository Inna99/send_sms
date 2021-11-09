# from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Text
from .serializers import TextSerializer

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response


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

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # payload = response.data
        #  send(payload)
        return response

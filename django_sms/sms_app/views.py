from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import TextSerializer
from .models import Text


class ListTextAPIView(ListAPIView):
    """This endpoint list all of the available texts from the database"""
    queryset = Text.objects.all()
    serializer_class = TextSerializer


class CreateTextAPIView(CreateAPIView):
    """This endpoint allows for creation of a text"""
    queryset = Text.objects.all()
    serializer_class = TextSerializer


class UpdateTextAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific text by passing in the id of the text to update"""
    queryset = Text.objects.all()
    serializer_class = TextSerializer


class DeleteTextAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Text from the database"""
    queryset = Text.objects.all()
    serializer_class = TextSerializer

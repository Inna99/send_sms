from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListTextAPIView.as_view(), name="text_list"),
    path("create/", views.CreateTextAPIView.as_view(), name="text_create"),
]

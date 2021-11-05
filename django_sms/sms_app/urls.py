from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListTextAPIView.as_view(), name="text_list"),
    path("create/", views.CreateTextAPIView.as_view(), name="text_create"),
    path("update/<int:pk>/", views.UpdateTextAPIView.as_view(), name="update_text"),
    path("delete/<int:pk>/", views.DeleteTextAPIView.as_view(), name="delete_text")
]

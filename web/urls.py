from django.contrib import admin
from django.urls import path, include
from .views import indexView, ProductDetails

# it is need for class based view
app_name = "web"

urlpatterns = [
    path("", indexView.as_view(), name="index"),
    path("details/<int:pk>", ProductDetails.as_view(), name="details"),
]

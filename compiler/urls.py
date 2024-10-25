from django.urls import path
from .views import upload_view

from django.urls import include

urlpatterns = [
    path('upload', upload_view.upload),
]
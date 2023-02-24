# example/urls.py
from django.urls import path

from betmomo.views import index


urlpatterns = [
    path('', index),
]
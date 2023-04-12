from apps.views import product
from django.urls import path

urlpatterns = [
    path('', product, name='products'),
]

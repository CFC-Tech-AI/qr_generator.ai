# urls.py
from django.urls import path
from .views import index, generate_qr

urlpatterns = [
    path('', index, name='index'),
    path('<int:data_id>/qr/', generate_qr, name='generate_qr'),
]

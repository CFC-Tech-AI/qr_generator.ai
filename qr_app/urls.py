from django.urls import path
from .views import index, generate_qr, clear_data

urlpatterns = [
    path('', index, name='index'),
    path('<int:data_id>/qr/', generate_qr, name='generate_qr'),
    path("clear_data/", clear_data, name="clear_data"),
]

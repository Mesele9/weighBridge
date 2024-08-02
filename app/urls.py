# urls.py
from django.urls import path
from . import views
from .utils import generate_receipt

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicle/entry/', views.vehicle_entry, name='vehicle_entry'),
    path('vehicle/exit/<int:pk>/', views.vehicle_exit, name='vehicle_exit'),
    path('vehicle/detail/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/receipt/<int:pk>/', generate_receipt, name='generate_receipt'),
    path('get_weight/', views.get_weight, name='get_weight'),  # Ensure this is correct

]


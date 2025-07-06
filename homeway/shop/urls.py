# shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('home/', views.home, name='home'),  # home route in shop app
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]

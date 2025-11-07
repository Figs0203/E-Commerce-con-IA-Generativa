from django.urls import path
from . import views

urlpatterns = [
    path('my-wishlist/', views.my_wishlist, name='my_wishlist'),
    path('toggle/<int:pk>/', views.toggle_wishlist, name='toggle_wishlist'),
]
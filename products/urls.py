from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.home, name='home'),

    path('product/create/', views.create_product, name='create_product'),
    path('product/bulk-create/', views.bulk_create_products, name='bulk_create_products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('products/',views.products, name='products'),

    # API endpoints
    path('api/products/bulk-create/', api_views.bulk_create_product, name='api_bulk_create_product'),

    #path('login/', views.user_login, name='login'),
    #path('logout/', views.user_logout, name='logout'),
    #path('register/', views.register, name='register'),
    #path('profile/', views.profile, name='profile' ),

    #path('about/', views.about, name='about'),

]

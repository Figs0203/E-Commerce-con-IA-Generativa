from django.urls import path, include
from . import views_simple as views

app_name = 'ai_api'

# URLs principales de la API de IA
urlpatterns = [
    # Endpoints principales
    path('generate/', views.generate_response, name='generate_response'),
    path('health/', views.health_check, name='health_check'),
    path('analyze-product/', views.analyze_product_image, name='analyze_product_image'),
]

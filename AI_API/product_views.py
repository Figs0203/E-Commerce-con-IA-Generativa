from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .services import ProductAIService
import logging

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    method='post',
    operation_description="Genera una descripción de producto usando IA",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'product_name': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre del producto'),
            'image_urls': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_STRING),
                description='URLs de imágenes del producto'
            ),
            'category': openapi.Schema(type=openapi.TYPE_STRING, description='Categoría del producto'),
        },
        required=['product_name']
    ),
)
@api_view(['POST'])
@permission_classes([AllowAny])
def generate_product_description(request):
    """
    Genera una descripción de producto usando IA
    """
    try:
        product_name = request.data.get('product_name')
        if not product_name:
            return Response(
                {'error': 'El campo product_name es requerido'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        image_urls = request.data.get('image_urls', [])
        category = request.data.get('category')
        user = request.user if request.user.is_authenticated else None
        
        product_ai_service = ProductAIService()
        result = product_ai_service.generate_product_description(
            product_name=product_name,
            image_urls=image_urls,
            category=category,
            user=user
        )
        
        if result['success']:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    except Exception as e:
        logger.error(f"Error in generate_product_description: {e}")
        return Response(
            {'error': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@swagger_auto_schema(
    method='post',
    operation_description="Analiza una imagen de producto usando IA",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'image_url': openapi.Schema(type=openapi.TYPE_STRING, description='URL de la imagen'),
            'product_name': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre del producto (opcional)'),
        },
        required=['image_url']
    ),
)
@api_view(['POST'])
@permission_classes([AllowAny])
def analyze_product_image(request):
    """
    Analiza una imagen de producto usando IA
    """
    try:
        image_url = request.data.get('image_url')
        if not image_url:
            return Response(
                {'error': 'El campo image_url es requerido'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        product_name = request.data.get('product_name')
        user = request.user if request.user.is_authenticated else None
        
        product_ai_service = ProductAIService()
        result = product_ai_service.analyze_product_image(
            image_url=image_url,
            product_name=product_name,
            user=user
        )
        
        if result['success']:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    except Exception as e:
        logger.error(f"Error in analyze_product_image: {e}")
        return Response(
            {'error': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@swagger_auto_schema(
    method='post',
    operation_description="Sugiere tags para un producto usando IA",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'product_name': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre del producto'),
            'description': openapi.Schema(type=openapi.TYPE_STRING, description='Descripción del producto'),
            'image_urls': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_STRING),
                description='URLs de imágenes del producto'
            ),
            'category': openapi.Schema(type=openapi.TYPE_STRING, description='Categoría del producto'),
        },
        required=['product_name', 'description']
    ),
)
@api_view(['POST'])
@permission_classes([AllowAny])
def suggest_product_tags(request):
    """
    Sugiere tags para un producto usando IA
    """
    try:
        product_name = request.data.get('product_name')
        description = request.data.get('description')
        
        if not product_name or not description:
            return Response(
                {'error': 'Los campos product_name y description son requeridos'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        image_urls = request.data.get('image_urls', [])
        category = request.data.get('category')
        user = request.user if request.user.is_authenticated else None
        
        product_ai_service = ProductAIService()
        result = product_ai_service.suggest_product_tags(
            product_name=product_name,
            description=description,
            image_urls=image_urls,
            category=category,
            user=user
        )
        
        if result['success']:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    except Exception as e:
        logger.error(f"Error in suggest_product_tags: {e}")
        return Response(
            {'error': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

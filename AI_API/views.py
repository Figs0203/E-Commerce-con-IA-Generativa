import base64

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .services import Gemma3Service, ProductAIService




@swagger_auto_schema(
    method='get',
    operation_description="Verifica el estado del servicio de IA",
)
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Verifica el estado del servicio de IA
    """
    try:
        gemma_service = Gemma3Service()
        health_status = gemma_service.health_check()
        
        if health_status['status'] == 'healthy':
            return Response(health_status, status=status.HTTP_200_OK)
        else:
            return Response(health_status, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
    except Exception as e:
        
        return Response(
            {'status': 'unhealthy', 'error': str(e)}, 
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )


@swagger_auto_schema(
    method='post',
    operation_description="Analiza una o múltiples imágenes de producto y genera información completa",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'image': openapi.Schema(type=openapi.TYPE_FILE, description='Archivo de imagen del producto'),
            'images': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_FILE), description='Múltiples imágenes del producto'),
        },
    ),
)
@api_view(['POST'])
@permission_classes([AllowAny])
def analyze_product_image_upload(request):
    """
    Analiza una o múltiples imágenes de producto subidas directamente y genera información completa para auto-llenar formulario
    """
    try:
        image_urls = []

        single_image = request.FILES.get('image')
        if single_image:
            image_urls.append(convert_image_to_data_url(single_image))

        multiple_images = request.FILES.getlist('images')
        for img in multiple_images:
            image_urls.append(convert_image_to_data_url(img))

        if not image_urls:
            return Response(
                {'error': 'No se proporcionó ninguna imagen'},
                status=status.HTTP_400_BAD_REQUEST
            )

        ai_service = ProductAIService()
        result = ai_service.analyze_product_complete(image_urls, user=request.user)

        if result['success']:
            return Response({
                'success': True,
                'data': result['data'],
                'request_id': result.get('request_id'),
                'processing_time': result.get('processing_time'),
                'images_analyzed': len(image_urls)
            })
        else:
            return Response({
                'success': False,
                'error': result.get('error', 'Error en el análisis de IA'),
                'raw_response': result.get('raw_response')
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:

        return Response(
            {'error': 'Error interno del servidor'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


def convert_image_to_data_url(image_file):
    """
    Convierte un archivo de imagen en una data URL base64
    """
    image_content = image_file.read()
    image_base64 = base64.b64encode(image_content).decode('utf-8')
    content_type = image_file.content_type or 'image/jpeg'
    return f"data:{content_type};base64,{image_base64}"
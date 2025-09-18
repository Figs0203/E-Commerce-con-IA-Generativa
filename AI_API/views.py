from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q

from .models import AIRequest, AIUsageStats, AIConfiguration, ProductAIGeneration
from .services import Gemma3Service, ProductAIService
from .serializers import (
    AIRequestSerializer, AIUsageStatsSerializer, 
    AIConfigurationSerializer, ProductAIGenerationSerializer
)
import logging

logger = logging.getLogger(__name__)



def generate_response(request):
    """
    Genera una respuesta usando el modelo Gemma 3
    """
    try:
        prompt = request.data.get('prompt')
        if not prompt:
            return Response(
                {'error': 'El campo prompt es requerido'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        image_urls = request.data.get('image_urls', [])
        max_tokens = request.data.get('max_tokens')
        temperature = request.data.get('temperature')
        request_type = request.data.get('request_type', 'chat')
        
        # Validar URLs de imágenes
        if image_urls and not isinstance(image_urls, list):
            return Response(
                {'error': 'image_urls debe ser una lista'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Obtener usuario si está autenticado
        user = request.user if request.user.is_authenticated else None
        
        # Generar respuesta
        gemma_service = Gemma3Service()
        result = gemma_service.generate_response(
            prompt=prompt,
            image_urls=image_urls,
            max_tokens=max_tokens,
            temperature=temperature,
            request_type=request_type,
            user=user
        )
        
        if result['success']:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    except Exception as e:
        logger.error(f"Error in generate_response: {e}")
        return Response(
            {'error': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


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
        logger.error(f"Error in health_check: {e}")
        return Response(
            {'status': 'unhealthy', 'error': str(e)}, 
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
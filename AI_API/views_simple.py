from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
import logging
import os
from urllib.parse import urljoin

logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["POST"])
def generate_response(request):
    """
    Genera una respuesta usando el modelo Gemma 3
    """
    try:
        data = json.loads(request.body)
        prompt = data.get('prompt')
        
        if not prompt:
            return JsonResponse(
                {'error': 'El campo prompt es requerido'}, 
                status=400
            )
        
        # Usar el servicio real de IA
        from .services import Gemma3Service
        
        gemma_service = Gemma3Service()
        result = gemma_service.generate_response(
            prompt=prompt,
            image_urls=data.get('image_urls', []),
            max_tokens=data.get('max_tokens'),
            temperature=data.get('temperature'),
            request_type=data.get('request_type', 'chat'),
            user=request.user if request.user.is_authenticated else None
        )
        
        if result['success']:
            return JsonResponse(result, status=200)
        else:
            return JsonResponse(result, status=500)
        
    except Exception as e:
        logger.error(f"Error in generate_response: {e}")
        return JsonResponse(
            {'error': 'Error interno del servidor'}, 
            status=500
        )


@require_http_methods(["GET"])
def health_check(request):
    """
    Verifica el estado del servicio de IA
    """
    try:
        # Usar el servicio real de IA
        from .services import Gemma3Service
        
        gemma_service = Gemma3Service()
        health_status = gemma_service.health_check()
        
        if health_status['status'] == 'healthy':
            return JsonResponse(health_status, status=200)
        else:
            return JsonResponse(health_status, status=503)
        
    except Exception as e:
        logger.error(f"Error in health_check: {e}")
        return JsonResponse(
            {'status': 'unhealthy', 'error': str(e)}, 
            status=503
        )


@csrf_exempt
@require_http_methods(["POST"])
def analyze_product_image(request):
    """
    Analiza una imagen de producto y genera información completa para auto-llenar formulario
    """
    try:
        image_file = request.FILES.get('image')
        
        if not image_file:
            return JsonResponse(
                {'error': 'No se proporcionó imagen'}, 
                status=400
            )
        
        # Convertir imagen a base64 para enviar directamente
        import base64
        
        # Leer el contenido de la imagen
        image_content = image_file.read()
        
        # Convertir a base64
        image_base64 = base64.b64encode(image_content).decode('utf-8')
        
        # Determinar el tipo MIME
        content_type = image_file.content_type or 'image/jpeg'
        
        # Crear URL de datos (data URL)
        image_url = f"data:{content_type};base64,{image_base64}"
        
        # Log para debugging
        logger.info(f"Image converted to data URL, size: {len(image_base64)} chars")
        
        # Importar el servicio de IA
        from .services import ProductAIService
        
        # Realizar análisis completo
        ai_service = ProductAIService()
        result = ai_service.analyze_product_complete(image_url, user=request.user)
        
        # No necesitamos limpiar archivos temporales ya que usamos data URLs
        
        if result['success']:
            return JsonResponse({
                'success': True,
                'data': result['data'],
                'request_id': result.get('request_id'),
                'processing_time': result.get('processing_time')
            })
        else:
            return JsonResponse({
                'success': False,
                'error': result.get('error', 'Error en el análisis de IA'),
                'raw_response': result.get('raw_response')
            }, status=500)
        
    except Exception as e:
        logger.error(f"Error in analyze_product_image: {e}")
        return JsonResponse(
            {'error': 'Error interno del servidor'}, 
            status=500
        )

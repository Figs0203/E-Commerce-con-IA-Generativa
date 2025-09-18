from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import AIRequest, AIUsageStats, AIConfiguration
from .serializers import AIRequestSerializer, AIUsageStatsSerializer, AIConfigurationSerializer
import logging

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    method='get',
    operation_description="Obtiene el historial de requests de IA del usuario",
    manual_parameters=[
        openapi.Parameter('request_type', openapi.IN_QUERY, description="Tipo de request", type=openapi.TYPE_STRING),
        openapi.Parameter('status', openapi.IN_QUERY, description="Estado del request", type=openapi.TYPE_STRING),
        openapi.Parameter('page', openapi.IN_QUERY, description="Número de página", type=openapi.TYPE_INTEGER),
    ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_requests(request):
    """
    Obtiene el historial de requests de IA del usuario autenticado
    """
    try:
        user_requests = AIRequest.objects.filter(user=request.user)
        
        # Filtros opcionales
        request_type = request.GET.get('request_type')
        status_filter = request.GET.get('status')
        
        if request_type:
            user_requests = user_requests.filter(request_type=request_type)
        if status_filter:
            user_requests = user_requests.filter(status=status_filter)
        
        # Paginación simple
        page = int(request.GET.get('page', 1))
        page_size = 20
        start = (page - 1) * page_size
        end = start + page_size
        
        requests_data = AIRequestSerializer(
            user_requests[start:end], 
            many=True
        ).data
        
        return Response({
            'requests': requests_data,
            'total': user_requests.count(),
            'page': page,
            'page_size': page_size
        })
        
    except Exception as e:
        logger.error(f"Error in get_user_requests: {e}")
        return Response(
            {'error': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@swagger_auto_schema(
    method='get',
    operation_description="Obtiene estadísticas de uso de IA del usuario",
    manual_parameters=[
        openapi.Parameter('days', openapi.IN_QUERY, description="Número de días hacia atrás", type=openapi.TYPE_INTEGER),
    ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_stats(request):
    """
    Obtiene estadísticas de uso de IA del usuario autenticado
    """
    try:
        days = int(request.GET.get('days', 30))
        
        # Obtener estadísticas de los últimos N días
        from django.utils import timezone
        from datetime import timedelta
        
        start_date = timezone.now().date() - timedelta(days=days)
        stats = AIUsageStats.objects.filter(
            user=request.user,
            date__gte=start_date
        ).order_by('-date')
        
        stats_data = AIUsageStatsSerializer(stats, many=True).data
        
        # Calcular totales
        total_requests = sum(stat['total_requests'] for stat in stats_data)
        total_tokens = sum(stat['total_tokens_used'] for stat in stats_data)
        successful_requests = sum(stat['successful_requests'] for stat in stats_data)
        
        return Response({
            'stats': stats_data,
            'totals': {
                'total_requests': total_requests,
                'successful_requests': successful_requests,
                'total_tokens_used': total_tokens,
                'success_rate': (successful_requests / total_requests * 100) if total_requests > 0 else 0
            },
            'period_days': days
        })
        
    except Exception as e:
        logger.error(f"Error in get_user_stats: {e}")
        return Response(
            {'error': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@swagger_auto_schema(
    method='get',
    operation_description="Obtiene detalles de una request específica",
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_request_detail(request, request_id):
    """
    Obtiene detalles de una request específica
    """
    try:
        ai_request = get_object_or_404(AIRequest, id=request_id, user=request.user)
        serializer = AIRequestSerializer(ai_request)
        return Response(serializer.data)
        
    except Exception as e:
        logger.error(f"Error in get_request_detail: {e}")
        return Response(
            {'error': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@swagger_auto_schema(
    method='get',
    operation_description="Obtiene la configuración actual de IA",
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_ai_configuration(request):
    """
    Obtiene la configuración actual de IA (solo para usuarios autenticados)
    """
    try:
        if not request.user.is_staff:
            return Response(
                {'error': 'Permisos insuficientes'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        config = AIConfiguration.objects.filter(is_active=True).first()
        if config:
            serializer = AIConfigurationSerializer(config)
            return Response(serializer.data)
        else:
            return Response(
                {'error': 'No hay configuración activa'}, 
                status=status.HTTP_404_NOT_FOUND
            )
            
    except Exception as e:
        logger.error(f"Error in get_ai_configuration: {e}")
        return Response(
            {'error': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

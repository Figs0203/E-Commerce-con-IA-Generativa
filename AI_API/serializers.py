from rest_framework import serializers
from .models import AIRequest, AIUsageStats, AIConfiguration, ProductAIGeneration
from django.contrib.auth.models import User


class AIRequestSerializer(serializers.ModelSerializer):
    """
    Serializer para requests de IA
    """
    user_username = serializers.CharField(source='user.username', read_only=True)
    has_images = serializers.BooleanField(read_only=True)
    is_multimodal = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = AIRequest
        fields = [
            'id', 'user', 'user_username', 'request_type', 'status',
            'prompt', 'image_urls', 'model_name', 'max_tokens', 'temperature',
            'response_text', 'response_tokens', 'processing_time',
            'created_at', 'updated_at', 'error_message',
            'has_images', 'is_multimodal'
        ]
        read_only_fields = [
            'id', 'user', 'status', 'response_text', 'response_tokens',
            'processing_time', 'created_at', 'updated_at', 'error_message',
            'has_images', 'is_multimodal'
        ]


class AIUsageStatsSerializer(serializers.ModelSerializer):
    """
    Serializer para estadísticas de uso de IA
    """
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = AIUsageStats
        fields = [
            'id', 'user', 'user_username', 'date',
            'total_requests', 'successful_requests', 'failed_requests',
            'total_tokens_used', 'product_description_requests',
            'image_analysis_requests', 'text_generation_requests',
            'chat_requests'
        ]
        read_only_fields = ['id', 'user']


class AIConfigurationSerializer(serializers.ModelSerializer):
    """
    Serializer para configuración de IA
    """
    class Meta:
        model = AIConfiguration
        fields = [
            'id', 'name', 'lightning_endpoint', 'api_key',
            'model_name', 'max_tokens_default', 'temperature_default',
            'timeout_seconds', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProductAIGenerationSerializer(serializers.ModelSerializer):
    """
    Serializer para generaciones de IA de productos
    """
    product_name = serializers.CharField(source='product.name', read_only=True)
    ai_request_id = serializers.IntegerField(source='ai_request.id', read_only=True)
    
    class Meta:
        model = ProductAIGeneration
        fields = [
            'id', 'product', 'product_name', 'ai_request', 'ai_request_id',
            'generation_type', 'original_content', 'ai_generated_content',
            'is_approved', 'is_used', 'created_at', 'approved_at'
        ]
        read_only_fields = [
            'id', 'ai_request', 'created_at', 'approved_at'
        ]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer básico para usuarios
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id', 'username']

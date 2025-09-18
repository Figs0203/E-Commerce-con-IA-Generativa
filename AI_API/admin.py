from django.contrib import admin
from .models import AIRequest, AIUsageStats, AIConfiguration, ProductAIGeneration


@admin.register(AIRequest)
class AIRequestAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'request_type', 'status', 'model_name',
        'response_tokens', 'processing_time', 'created_at'
    ]
    list_filter = ['request_type', 'status', 'model_name', 'created_at']
    search_fields = ['prompt', 'response_text', 'user__username']
    readonly_fields = ['created_at', 'updated_at', 'processing_time']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('user', 'request_type', 'status', 'model_name')
        }),
        ('Request', {
            'fields': ('prompt', 'image_urls', 'max_tokens', 'temperature')
        }),
        ('Response', {
            'fields': ('response_text', 'response_tokens', 'processing_time', 'error_message')
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AIUsageStats)
class AIUsageStatsAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'date', 'total_requests', 'successful_requests',
        'failed_requests', 'total_tokens_used'
    ]
    list_filter = ['date', 'user']
    search_fields = ['user__username']
    readonly_fields = ['date']
    ordering = ['-date']


@admin.register(AIConfiguration)
class AIConfigurationAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'model_name', 'lightning_endpoint', 'is_active',
        'max_tokens_default', 'temperature_default'
    ]
    list_filter = ['is_active', 'model_name']
    search_fields = ['name', 'lightning_endpoint']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Configuración', {
            'fields': ('name', 'is_active')
        }),
        ('Endpoint', {
            'fields': ('lightning_endpoint', 'api_key')
        }),
        ('Modelo', {
            'fields': ('model_name', 'max_tokens_default', 'temperature_default', 'timeout_seconds')
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ProductAIGeneration)
class ProductAIGenerationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'product', 'generation_type', 'is_approved',
        'is_used', 'created_at'
    ]
    list_filter = ['generation_type', 'is_approved', 'is_used', 'created_at']
    search_fields = ['product__name', 'ai_generated_content']
    readonly_fields = ['created_at', 'approved_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Producto y Request', {
            'fields': ('product', 'ai_request', 'generation_type')
        }),
        ('Contenido', {
            'fields': ('original_content', 'ai_generated_content')
        }),
        ('Estado', {
            'fields': ('is_approved', 'is_used', 'approved_at')
        }),
        ('Metadatos', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
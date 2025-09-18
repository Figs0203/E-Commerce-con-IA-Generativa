from django.core.management.base import BaseCommand
from AI_API.models import AIConfiguration


class Command(BaseCommand):
    help = 'Configura la configuración inicial de IA'

    def handle(self, *args, **options):
        # Crear configuración por defecto si no existe
        config, created = AIConfiguration.objects.get_or_create(
            name='default',
            defaults={
                'lightning_endpoint': 'https://8001-01k4ap2fswtrsc3fyamsj261fp.cloudspaces.litng.ai',
                'api_key': 'gemma3-litserve',
                'model_name': 'google/gemma-3-4b-it',
                'max_tokens_default': 256,
                'temperature_default': 0.7,
                'timeout_seconds': 300,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS('Configuración de IA creada exitosamente')
            )
        else:
            self.stdout.write(
                self.style.WARNING('La configuración de IA ya existe')
            )
        
        self.stdout.write(f'Endpoint: {config.lightning_endpoint}')
        self.stdout.write(f'Modelo: {config.model_name}')
        self.stdout.write(f'Activo: {config.is_active}')

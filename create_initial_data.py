#!/usr/bin/env python
"""
⚠️  ARCHIVO OBSOLETO - NO USAR ⚠️

Este archivo ha sido reemplazado por un sistema automático mejor.

✅ USAR EN SU LUGAR:
   python manage.py setup_categories

📚 Ver SETUP.md para más información
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productplatform.settings')
django.setup()

from products.models import Category, Product
from django.contrib.auth.models import User

def create_initial_data():
    print("Creando datos iniciales...")
    
    # Crear categorías
    categories = [
        {'name': 'Electrónica', 'description': 'Productos electrónicos y tecnológicos'},
        {'name': 'Ropa', 'description': 'Vestimenta y accesorios'},
        {'name': 'Hogar', 'description': 'Artículos para el hogar y decoración'},
        {'name': 'Deportes', 'description': 'Equipamiento y ropa deportiva'},
        {'name': 'Libros', 'description': 'Libros, revistas y material educativo'},
        {'name': 'Juguetes', 'description': 'Juguetes y entretenimiento'},
        {'name': 'Automóviles', 'description': 'Partes y accesorios para vehículos'},
        {'name': 'Jardín', 'description': 'Productos para jardín y exteriores'},
    ]
    
    created_categories = []
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            print(f"✅ Categoría creada: {category.name}")
        else:
            print(f"ℹ️  Categoría ya existe: {category.name}")
        created_categories.append(category)
    
    # Crear usuario de ejemplo si no existe
    user, created = User.objects.get_or_create(
        username='usuario_ejemplo',
        defaults={
            'email': 'ejemplo@test.com',
            'first_name': 'Usuario',
            'last_name': 'Ejemplo'
        }
    )
    if created:
        user.set_password('password123')
        user.save()
        print("✅ Usuario de ejemplo creado: usuario_ejemplo / password123")
    else:
        print("ℹ️  Usuario de ejemplo ya existe")
    
    # Crear algunos productos de ejemplo
    sample_products = [
        {
            'title': 'Smartphone Samsung Galaxy',
            'description': 'Smartphone de última generación con cámara de alta resolución y pantalla AMOLED de 6.7 pulgadas. Incluye 128GB de almacenamiento y 8GB de RAM.',
            'price': 599.99,
            'category': 'Electrónica',
            'status': 'published'
        },
        {
            'title': 'Camiseta de Algodón Orgánico',
            'description': 'Camiseta 100% algodón orgánico, cómoda y respirable. Disponible en varios colores y tallas. Perfecta para uso diario.',
            'price': 24.99,
            'category': 'Ropa',
            'status': 'published'
        },
        {
            'title': 'Lámpara de Mesa LED',
            'description': 'Lámpara de mesa moderna con tecnología LED, ajustable en intensidad y temperatura de color. Ideal para escritorio o mesita de noche.',
            'price': 45.50,
            'category': 'Hogar',
            'status': 'published'
        },
        {
            'title': 'Balón de Fútbol Profesional',
            'description': 'Balón de fútbol de alta calidad, tamaño 5, perfecto para entrenamientos y partidos. Material resistente y durabilidad garantizada.',
            'price': 89.99,
            'category': 'Deportes',
            'status': 'published'
        },
        {
            'title': 'Libro: El Arte de la Guerra',
            'description': 'Clásico de Sun Tzu sobre estrategia militar y liderazgo. Edición especial con comentarios y análisis modernos.',
            'price': 19.99,
            'category': 'Libros',
            'status': 'published'
        }
    ]
    
    for product_data in sample_products:
        category = Category.objects.get(name=product_data['category'])
        product, created = Product.objects.get_or_create(
            title=product_data['title'],
            defaults={
                'description': product_data['description'],
                'price': product_data['price'],
                'category': category,
                'seller': user,
                'status': product_data['status']
            }
        )
        if created:
            print(f"✅ Producto creado: {product.title}")
        else:
            print(f"ℹ️  Producto ya existe: {product.title}")
    
    print("\n🎉 Datos iniciales creados exitosamente!")
    print(f"📊 Total de categorías: {Category.objects.count()}")
    print(f"📦 Total de productos: {Product.objects.count()}")
    print(f"👥 Total de usuarios: {User.objects.count()}")

if __name__ == '__main__':
    create_initial_data()

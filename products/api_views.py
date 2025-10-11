from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Product, Category


@login_required
@require_http_methods(["POST"])
def bulk_create_product(request):
    """
    API endpoint para crear un producto individual desde carga masiva
    """
    try:
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        suggested_category = request.POST.get('suggested_category')
        status = request.POST.get('status', 'draft')

        if not image:
            return JsonResponse({
                'success': False,
                'error': 'No se proporcionó imagen'
            }, status=400)

        if not title or not description:
            return JsonResponse({
                'success': False,
                'error': 'Título y descripción son requeridos'
            }, status=400)

        category = None
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                pass

        if not category and suggested_category:
            category = Category.objects.filter(
                name__icontains=suggested_category
            ).first()

        if not category:
            category = Category.objects.first()

        if not category:
            return JsonResponse({
                'success': False,
                'error': 'No hay categorías disponibles en el sistema'
            }, status=400)

        try:
            price_value = float(price) if price else 0.0
            if price_value < 0:
                price_value = 0.0
        except (ValueError, TypeError):
            price_value = 0.0

        product = Product.objects.create(
            title=title,
            description=description,
            price=price_value,
            category=category,
            image=image,
            seller=request.user,
            status=status
        )


        return JsonResponse({
            'success': True,
            'product': {
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'price': str(product.price),
                'category': product.category.name,
                'status': product.status,
            }
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Error creando producto: {str(e)}'
        }, status=500)
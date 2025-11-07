from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist


@login_required
def my_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related("product")
    return render(request, 'wishlist/my_wishlist.html', {"wishlist_items": wishlist_items})


@login_required
def toggle_wishlist(request, pk):
    product = get_object_or_404(Product, pk=pk)

    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if not created:
        # Si ya existía, lo quitamos
        wishlist_item.delete()

    return redirect('product_detail', pk=pk)
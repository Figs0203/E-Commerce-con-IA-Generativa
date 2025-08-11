from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Título del producto")
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")
    image = models.ImageField(upload_to='products/images/', verbose_name="Imagen del producto")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Vendedor")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
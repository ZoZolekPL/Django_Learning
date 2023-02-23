from django.shortcuts import render, get_object_or_404
from .models import Categories, Products

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Categories.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categories, slug = category_slug)
        products = products.filter(category=category)
    return  render(request, '')

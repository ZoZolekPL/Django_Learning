from django.shortcuts import render, get_object_or_404
from .models import Categories, Products

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Categories.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categories,
                                     slug = category_slug)
        products = products.filter(category=category)
    return  render(request, 'shopapp/html/products_list.html', {'category':category,
                                                                'categories':categories,
                                                                'products':products})

def products_details(request, id, slug):
    product = get_object_or_404(Products,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'shopapp/html/products_detail.html',
                  {'product':product})
from django.contrib import admin
from.models import Categories, Products

# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available', 'price']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug' : ('name',)}
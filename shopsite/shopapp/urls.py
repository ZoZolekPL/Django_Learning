from django.urls import path
from . import views


app_name = 'shopapp'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='products_list_by_category'),
    path('<int:id>/slug:slug/', views.products_details, name= 'products_detail'),
]
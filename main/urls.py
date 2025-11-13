from django.urls import path
from .import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('create-product', views.createProduct, name='create-product'),
    path('delete-product/<int:pk>/', views.deleteProduct, name='delete-product'),
    path('get-product/<int:pk>/', views.getProduct, name='get-product')
]

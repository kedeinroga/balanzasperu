from django.urls import path
from .views import ProductListView, ProductDetailView

product_patterns = ([
    path('', ProductListView.as_view(), name='products'),
    path('<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='product'),
], 'product')
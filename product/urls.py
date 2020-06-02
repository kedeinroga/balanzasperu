from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryDetailView

product_patterns = ([
    path('', ProductListView.as_view(), name='products'),
    path('<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('category/<int:pk>/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
], 'product')
from django.urls import path
from .views import ServicesListView, ServicesDetailView, CategoryDetailView

services_patterns = ([
    path('', ServicesListView.as_view(), name='services'),
    path('<int:pk>/<slug:slug>/', ServicesDetailView.as_view(), name='service'),
    path('category/<int:pk>/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
], 'services')
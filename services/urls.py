from django.urls import path
from .views import ServicesListView, ServicesDetailView

services_patterns = ([
    path('', ServicesListView.as_view(), name='services'),
    path('<int:pk>/<slug:slug>/', ServicesDetailView.as_view(), name='service'),
    
], 'services')
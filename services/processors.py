from .models import Category
from django import template


def ctx_dict(request):
    return {'services_context':Category.objects.order_by('name')} 


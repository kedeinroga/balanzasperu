from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from blog.models import Post, Category
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    paginate_by = 6
    
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
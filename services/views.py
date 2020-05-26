from django.shortcuts import render
from .models import Service
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Post, Category
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class ServicesListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    paginate_by = 6


class ServicesDetailView(DetailView):
    model = Service
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

    def get(self, request, *args, **kwargs):
        service = Service.objects.all()
        category = Category.objects.all()
        post_list = Post.objects.all().order_by('-id')
        context = {'category':category, 'post_list':post_list, 'service':service}
        return render(request, self.template_name, context)

class ServicesDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'

    def get(self, request, *args, **kwargs):
        service = Service.objects.all()
        category = Category.objects.all()
        post_list = Post.objects.all().order_by('-id')
        context = {'category':category, 'post_list':post_list, 'service':service}
        return render(request, self.template_name, context)
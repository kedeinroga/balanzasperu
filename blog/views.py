from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class BlogListView(ListView):
    model = Post
    #post_list = Post.objects.all().order_by('-id')
    template_name = 'blog/post_list.html'
    paginate_by = 6

    
    
    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    

class CategoryDetailView(DetailView):
    
    
    model = Category
    template_name = 'blog/category_detail.html'
    
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #category = Category.objects.all()
        #post_list = Post.objects.all().order_by('-id')
        #context = {'category':category, 'post_list':post_list}
        #print(context)
        #return context
    


    

   


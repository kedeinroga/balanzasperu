from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
#class Category(MPTTModel):
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    #parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    class MPTTMeta:
        order_insertion_by = ['name']
    
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ('category')



class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']
        

    def __str__(self):
        return self.title
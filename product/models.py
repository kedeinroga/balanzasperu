from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']
    
    

    def __str__(self):
        return self.name

class Product(models.Model):
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_products")
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="product")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-created']

    def __str__(self):
        return self.title

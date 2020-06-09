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
    description = models.CharField(verbose_name="Descripcion del producto", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    codigo = models.CharField(verbose_name="Código", max_length=20, unique=True)
    precio = models.FloatField(verbose_name="Precio", default=0)
    numparte = models.CharField(verbose_name="Número de parte", max_length=50)
    image1 = models.ImageField(verbose_name="Imagen principal", upload_to="product")
    image2 = models.ImageField(verbose_name="Imagen secundaria", upload_to="product")
    image3 = models.ImageField(verbose_name="Imagen secundaria 2", upload_to="product")
    video = models.FileField(verbose_name="Video", upload_to="product")
    hojadatos = models.FileField(verbose_name="Hoja de datos", upload_to="product")
    aplicaciones = models.FileField(verbose_name="Lista de aplicaciones", upload_to="product")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        unique_together = ['codigo']
        ordering = ['-created']

    def __str__(self):
        return self.title

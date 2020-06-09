from django.contrib import admin

from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published','codigo', 'precio', 'product_categories')
    ordering = ('title','published')
    search_fields = ('title','content', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('title','categories__name')

    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }

    def product_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    product_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

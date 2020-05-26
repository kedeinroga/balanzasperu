from django.contrib import admin
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoryAdmin2(MPTTModelAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_post_count', 'related_post_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Post.objects.add_related_count(
                qs,
                Post,
                'category',
                'post_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Post.objects.add_related_count(qs,
                 Post,
                 'category',
                 'post_count',
                 cumulative=False)
        return qs

    def related_post_count(self, instance):
        return instance.post_count
    related_post_count.short_description = 'Related post (for this specific category)'

    def related_post_cumulative_count(self, instance):
        return instance.post_cumulative_count
    related_post_cumulative_count.short_description = 'Related post (in tree)'

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','content','author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Post, PostAdmin)

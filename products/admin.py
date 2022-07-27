from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    # sets up values for how admin site list products
    list_display = ['name', 'brand', 'sku', 'price', 'old_price', 'created', 'updated']
    list_display_links = ('name', )
    list_per_page = 50
    ordering = ['-created']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('create', 'updated')
    # sets up slug to be generated from product name
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    # set up values for how admin site lists categories
    list_display = ['name', 'created', 'updated']
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created', 'updated',)

    # Sets up slug to be generated from product name
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Category, CategoryAdmin)



from django.contrib import admin

# Register your models here.

from .models import Category, Product

# Admin customization for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display ID and Name in the admin list view
    search_fields = ('name',)  # Enable search by name
    list_per_page = 10  # Limit number of categories shown per page

# Admin customization for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')  # Show key details
    list_filter = ('category',)  # Filter products by category
    search_fields = ('name', 'description')  # Search by name and description
    list_per_page = 20  # Limit number of products shown per page
    ordering = ('name',)  # Default ordering by name

# Register the models with admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

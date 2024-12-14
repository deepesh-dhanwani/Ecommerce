from django.contrib import admin

# Register your models here.

from .models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_on')
    search_fields = ('user__username', 'product__name')

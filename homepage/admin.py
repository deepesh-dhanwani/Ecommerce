from django.contrib import admin
from homepage.models import homepage
from homepage.models import homepageright
from homepage.models import Brandimg
from homepage.models import featureproduct
# Register your models here.

class homepageAdmin(admin.ModelAdmin):
    list_display = ('homepage_desc','homepage_button','homepage_img')
admin.site.register(homepage,homepageAdmin)

class homepagerightAdmin(admin.ModelAdmin):
    list_display=('homepageright_text','homepageright_img')
admin.site.register(homepageright,homepagerightAdmin)

class BrandimgAdmin(admin.ModelAdmin):
    list_display=('id','Brand_img')
admin.site.register(Brandimg,BrandimgAdmin)

class Featureproduct(admin.ModelAdmin):
    list_display=('product_name','product_image','product_price','product_rating','product_desc')
admin.site.register(featureproduct,Featureproduct)
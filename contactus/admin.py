from django.contrib import admin
from contactus.models import Contactform
# Register your models here.

class Contactformadmin(admin.ModelAdmin):
    list_display=('fullname','email','subject','message')
admin.site.register(Contactform,Contactformadmin)
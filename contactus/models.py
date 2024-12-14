from django.db import models

# Create your models here.
class Contactform(models.Model):
    fullname= models.CharField(max_length=250,blank=False)
    email=models.CharField(max_length=500,blank=False)
    subject=models.TextField(blank=False)
    message=models.TextField(blank=False)
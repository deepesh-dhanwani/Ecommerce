from django.db import models

# Create your models here.
class homepage(models.Model):
    homepage_desc=models.CharField(max_length=500)
    homepage_button= models.CharField(max_length=250)
    homepage_img=models.FileField(upload_to="homepage",max_length=500,null=True,default=None)

class homepageright(models.Model):
    homepageright_text=models.TextField()
    homepageright_img=models.FileField(upload_to="homepageright",max_length=500,null=True,default=None)

class Brandimg(models.Model):
    id = models.AutoField(primary_key=True)
    Brand_img=models.FileField(upload_to="Brandimg",max_length=500,null=True,default=None)

class featureproduct(models.Model):
    product_name= models.CharField(max_length=500)
    product_image = models.FileField(upload_to="featureproduct",max_length=500,null=False,default=None)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    product_rating=models.FloatField()
    product_desc=models.TextField(blank=True,null=True)
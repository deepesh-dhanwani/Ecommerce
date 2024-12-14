from django.db import models

# Create your models here.

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)  # e.g., Male, Female, Child

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)  # e.g., T-shirt, Jeans
    description = models.TextField()  # Description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Product image

    def __str__(self):
        return self.name

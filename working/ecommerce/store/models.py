from django.db import models
from User.models import *
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=25)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    details= models.TextField()
    oldPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"{self.name} , {self.price}" 


class Basket(models.Model): #aka cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=10 , default='notyet')
    total = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)
    def __str__(self):
        return f"{self.product} , {self.quantity}"

class Order(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    order_item= models.ManyToManyField(Product)



# Create your models here.
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=300)
    date_registration = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_product = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='media/')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(default=timezone.now)

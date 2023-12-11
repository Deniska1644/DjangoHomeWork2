from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=300)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'name : {self.name}, email: {self.email}, phone number: {self.phone_number},'
                f'adres: {self.address}, date registration: {self.date_registration}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_product = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='media/')

    def __str__(self):
        return (f'name: {self.name}, description: {self.description},price: {self.price},'
                f'quantity: {self.quantity_product}')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f'customer: {self.customer}, product: {self.products}, total price: {self.total_price},'
                f'date order: {self.date_ordered}')
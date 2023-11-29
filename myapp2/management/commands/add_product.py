from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            product = Product(name=f'product {i}', description=f'{i * 9}', price=i * 0.6, quantity_product=i)
            product.save()
            self.stdout.write(f'{product}')

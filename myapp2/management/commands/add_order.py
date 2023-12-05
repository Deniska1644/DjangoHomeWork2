from django.core.management.base import BaseCommand
from myapp2.models import Order, User, Product


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            order = Order(customer=User.objects.get(id=1),
                          total_price=14.22)
            order.save()
            order.products.add(Product.objects.get(id=i))
            self.stdout.write(f'{order}')

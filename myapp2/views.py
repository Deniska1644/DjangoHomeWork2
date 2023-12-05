from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Order
from datetime import datetime, timedelta


def index(request):
    return HttpResponse('Hi')


# def get_users(request):
#     id_user = User.objects.name(pk=1)
#     context = {"id_user_name": id_user}
#     return render(request, 'myapp2/show_orders.html', context)

# def get_users(request, id_user):
#     name = User.objects.get(pk=id_user)
#     context = {
#         "id_user_name": name.email,
#     }
#     print(type(name))
#     return render(request, 'myapp2/show_orders.html', context)

def get_orders(request, id_user):
    user = get_object_or_404(User, pk=id_user)
    order = Order.objects.filter(customer=user)
    date = datetime.now()
    if request.method == 'POST':
        choice = int(request.POST.get('choice', 100))
        delta = date - timedelta(days=choice)
        context = {
            'order': order.filter(date_ordered__range=(delta, date)),
            'user': user.name
        }
        print(date)
        return render(request, 'myapp2/show_orders.html', context)

    else:
        context = {
            'order': order,
            'user': user.name
        }
    return render(request, 'myapp2/show_orders.html', context)



from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import User, Order, Product
from datetime import datetime, timedelta
from .forms import UserForm, AddImage


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


def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            user = User(name=name, email=email,
                        phone_number=phone_number, address=address)
            user.save()
            print(user.name)
            return render(request, 'myapp2/user_form.html', {'context': 'user added'})
    else:
        form = UserForm()
        return render(request, 'myapp2/user_form.html', {'form': form})


def add_image_product(request):
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():
            id_image = form.cleaned_data['id_image']
            image = form.cleaned_data['image']
            product = get_object_or_404(Product, pk=id_image)
            product.image = image
            product.save()
        return render(request, 'myapp2/user_form.html', {'context': 'image added'})
    else:
        form = AddImage()
    return render(request, 'myapp2/user_form.html', {'form': form})

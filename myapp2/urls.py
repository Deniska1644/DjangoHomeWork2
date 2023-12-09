from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('about/<int:id_user>', views.get_users, name='get_users'),
    path('orders/<int:id_user>', views.get_orders, name='get_orders'),
    path('user', views.user_form, name='user_form'),
    path('addimage', views.add_image_product, name=' add_image_product'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('about/<int:id_user>', views.get_users, name='get_users'),
    path('orders/<int:id_user>', views.get_orders, name='get_orders'),
]

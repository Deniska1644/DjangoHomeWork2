from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    return HttpResponse('Hi')


def get_users(request):
    return HttpResponse(User.objects.all())

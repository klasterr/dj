from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

def index(request):
    users = auth.objects.all()
    context = {
        'title': 'Головна сторінка',
        'users': users,
    }
    return render(request, 'main/index.html', context=context)

def user(reuqest, user_id):
    return HttpResponse(f"Сторінка користувача: {user_id}")

def news(request):
    context = {
        'title': 'Новини'
    }
    return render(request, 'main/news.html', context=context)

def post(request):
    context = {
        'title': 'Публікація'
    }
    return render(request, 'main/news.html', context=context)

def attractions(request):
    context = {
        'title': "Пам'ятки"
    }
    return render(request, 'main/news.html', context=context)

def account(request):
    context = {
        'title': 'Акаунт'
    }
    return render(request, 'main/news.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("Сторінку не найднено!")

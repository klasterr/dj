from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
from .forms import articleForm

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
    if request.method == "POST":
        form = articleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    form = articleForm()

    context = {
        'title': 'Публікація',
        'form': form,
    }
    return render(request, 'main/post.html', context=context)

def attractions(request):
    context = {
        'title': "Пам'ятки"
    }
    return render(request, 'main/attractions.html', context=context)

def account(request):
    context = {
        'title': 'Акаунт'
    }
    return render(request, 'main/account.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("Сторінку не найднено!")

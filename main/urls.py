from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('user/<int:user_id>/', user, name='user'),
    path('news/', news, name='news'),
    path('post/', post, name='post'),
    path('attractions/', attractions, name='attractions'),
    path('account/', account, name='account')
]
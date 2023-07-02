from django.contrib import admin
from .models import *

class authAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'email', 'password', 'date')
    list_display_links = ('id', 'nickname')
    search_fields = ('nickname', 'email')

class articleAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'author', 'description', 'date', 'views', 'likes', 'photo')

admin.site.register(auth, authAdmin)
admin.site.register(article, articleAdmin)
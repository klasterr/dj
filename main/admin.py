from django.contrib import admin
from .models import *

class authAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'email', 'password', 'date')
    list_display_links = ('id', 'nickname')
    search_fields = ('nickname', 'email')

admin.site.register(auth, authAdmin)
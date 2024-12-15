from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin) :
    list_display = ('title' , 'datetime_create' , 'datetime_update' ,'status')

admin.site.register(Post , PostAdmin)
from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('' , views.show_post , name='show') ,
    path('detail/<int:id>/' , views.show_detail_post , name='detail') ,
    path('create/' , views.create_post , name='create') ,
]
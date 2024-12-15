from django.shortcuts import render
from .models import *
# Create your views here.

def show_post(request):
    posts = Post.objects.filter(status='pub')
    return render(request , 'home.html' , {'posts':posts})

def show_detail_post(request, id):
    post = Post.objects.get(id=id)
    return render(request , 'detail.html' , {'post':post})


def create_post(request):
    print(request.POST)

    if request.method == 'POST' :
        print(request.POST.get('title'))
        print(request.POST.get('information'))

        a = request.POST.get('title')
        b = request.POST.get('information')
        Post.objects.create(title = a , information= b , status='drf')
    else :
        pass
    return render(request , 'create_post.html')
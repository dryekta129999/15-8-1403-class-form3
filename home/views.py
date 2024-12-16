from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import NewPostForm
def show_post(request):
    posts = Post.objects.filter(status='pub')
    return render(request , 'home.html' , {'posts':posts})

def show_detail_post(request, id):
    post = Post.objects.get(id=id)
    return render(request , 'detail.html' , {'post':post})






def create_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:show')  # Redirect to the post list or another appropriate view
    else:
        form = NewPostForm()
    return render(request, 'create_post.html', {'form': form})


def update_post(request,id):
    # post = Post.objects.get(id=id)
    post=get_object_or_404(Post, id=id)

    form = NewPostForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('home:show')


    return render(request,'create_post.html',{'form':form})

def delete_post(request,id):
    post=get_object_or_404(Post, id=id)
    if request.method=='POST':
        post.delete()
        return redirect('home:show')
    return render(request,'delete.html',{'post':post})
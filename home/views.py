from django.shortcuts import render, redirect
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

from django.shortcuts import render
from .models import BlogPost

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog/detail.html', {'post': post})

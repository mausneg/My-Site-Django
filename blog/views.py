from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.http import Http404
from .models import Post, Author, Tag

posts_data = Post.objects.all().order_by("-date")

def index(request):
    latest_post = posts_data[:3]
    print(latest_post)
    return render(request, "blog/index.html", {
        "posts": latest_post
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "posts": posts_data
    })

def post_detail(request, slug):
    selected_post = next((post for post in posts_data if post.slug == slug) , None)
    if selected_post is None:
        raise Http404()
    return render(request, "blog/post-detail.html", {
        'post': selected_post
    })
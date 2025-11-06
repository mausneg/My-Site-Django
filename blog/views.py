from django.shortcuts import render
from django.http import HttpResponse

user = {
    "username": "mausneg",
    "profile_path": ""
}

def index(request):
    return render(request, "blog/index.html", {
        "user": user
    })

def all_posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html",{
        'slug': slug
    })
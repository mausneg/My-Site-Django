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

def posts(request):
    return HttpResponse("posts")

def post_detail(request, slug):
    return HttpResponse(slug)
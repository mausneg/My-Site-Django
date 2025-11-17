from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment
from .forms import CommentForm

class HomeView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by("-date")[:3]

class PostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "form": CommentForm(),
            "tag": post.tag.all(),
            "comments": post.comments.all().order_by("-datetime")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        return render(request, "blog/post-detail.html", {
            "post": post,
            "form": form,
            "tags": post.tag.all(),
            "comments": post.comments.all().order_by("-datetime")
        })
    
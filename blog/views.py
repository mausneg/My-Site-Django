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

class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["tags"] = self.object.tag.all()
        return context
    
class SaveComment(View):
    def post(self, request):
        slug = request.POST["slug"]
        post = Post.objects.get(slug=slug)
        comment = Comment(
            username=request.POST["username"],
            email=request.POST["email"],
            text=request.POST["text"],
            post=post
        )
        comment.save()
        return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
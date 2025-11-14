from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="starting-page"),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    path("posts/comment", views.SaveComment.as_view(), name="posts-comment"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page")
]

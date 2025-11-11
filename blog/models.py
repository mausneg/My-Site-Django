from django.db import models
from django.urls import reverse


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_fullname()
class Post(models.Model):
    title = models.CharField(max_length=50)
    image_name = models.URLField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag, related_name="posts")
    content = models.TextField(null=True)
    excerpt = models.TextField()

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} - {self.author}"


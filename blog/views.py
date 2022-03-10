from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse

class BlogView(generic.ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    
class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    queryset = Post.objects.all()
    
    
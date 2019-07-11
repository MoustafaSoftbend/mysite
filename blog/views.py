from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post, Image

# Create your views here.

def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    stuff_for_frontend = {'posts': post,}
    return render(request,'blog/post_list.html',stuff_for_frontend)
from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from django.shortcuts import render
from .models import post, Category

def home(request):
    posts = post.objects.all()
    categories = Category.objects.all()
    context = {
       "posts": posts,
       "categories": categories,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
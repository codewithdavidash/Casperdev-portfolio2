from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    products = Project.objects.all()[:3]
    context = {
        'p': products
    }
    return render(request, 'core/index.html', context=context)


def  about(request):
    context = {}
    return render(request, 'core/about.html', context)


def contact(request):
    context = {}
    return render(request, 'core/contact.html', context)

def project(request):
    products = Project.objects.all()
    context = {
        'p': products
    }
    return render(request, 'core/project.html', context)


def services(request):
    return render(request, 'core/services.html')


def blog(request):
    posts = Blog.objects.all().order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'core/blog.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'core/blog_detail.html', context)

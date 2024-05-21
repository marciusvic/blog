from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    showSearch = True
    return render(request, 'home.html', {'posts': posts, 'showSearch': showSearch})

def gds(request):
    return render(request, 'gds.html')

def consultoria(request):
    return render(request, 'consultoria.html')

# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from db.models import Post, Category



def home(request):
    latest_project = Post.get_lastest_visible('project')
    latest_blog = Post.get_lastest_visible('blog')
    latest_arabic = Post.get_lastest_visible('arabic')

    return render(request, 'home.html', {
        'latest_project': latest_project,
        'latest_blog': latest_blog,
        'latest_arabic':latest_arabic,
    })

def cv(request):
    return render(request, 'cv.html',)

def smedia(request):
    return render(request, 'smedia.html',)

def contact(request):
    return render(request, 'contact.html',)

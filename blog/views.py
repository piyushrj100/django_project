from django.shortcuts import render
from django.http import Http404, HttpResponse

posts = [
    {
        'author': 'Piyush',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 29, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 29, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request) :
    #return HttpResponse('<h1>About Blog</h1>')
    return render(request,'blog/about.html')

# Create your views here.

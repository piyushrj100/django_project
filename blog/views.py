from django.shortcuts import render
from django.http import Http404, HttpResponse

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html')

def about(request) :
    #return HttpResponse('<h1>About Blog</h1>')
    return render(request,'blog/about.html')

# Create your views here.

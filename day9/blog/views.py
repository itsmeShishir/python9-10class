from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 2 tyoes of views class and function based views
# def home(request):
#     return HttpResponse("<h1>My name is shishir</h1>")

# def About(request):
#     return HttpResponse("<h1>this is about page</h1>")

# show html template in this page
def home(request):
    return render(request, 'index.html')

def categories(request):
    return render(request, 'category.html')

def single(request):
    return render(request, 'single.html')

def contact(request):
    return render(request, 'contact.html')

def createBlog(request):
    return render(request, 'create_blog.html')


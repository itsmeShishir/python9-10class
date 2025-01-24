from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Blog, Category, Contact
# Create your views here.
# 2 tyoes of views class and function based views
# def home(request):
#     return HttpResponse("<h1>My name is shishir</h1>")

# def About(request):
#     return HttpResponse("<h1>this is about page</h1>")

# show html template in this page
def home(request):
    # asc order  by id in categories
    categories = Category.objects.all().order_by('-id')
    # isslider in mobdel
    slider = Blog.objects.filter(isSlider=True) 
    featured = Blog.objects.filter(isFeatured=True)
    blogs = Blog.objects.all()
    # show only 4 blogs in home page
    onlyfour = Blog.objects.all()[:4]

    context = {
        'categories': categories,
        'blogs': blogs,
        'slider': slider,
        'featured': featured,
        'onlyfour': onlyfour
    }
    return render(request, 'index.html', context)

def categories(request, id):
    category = Category.objects.get(id=id)
    # check the id form the blgos
    blogs = Blog.objects.filter(category=category)
    context = {
        'category': category,
        'blogs': blogs
    }

    return render(request, 'category.html', context)

def getallblogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'allblogs.html', context)

def single(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, 'single.html', context)

def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # if message successful redirec to home page
        Contact.objects.create(
            fullname=fullname,
            email=email,
            subject=subject,
            message=message
        )
        return redirect('home')

    return render(request, 'contact.html')

def createBlog(request):
    return render(request, 'create_blog.html')


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 2 tyoes of views class and function based views
def home(request):
    return HttpResponse("<h1>My name is shishir</h1>")

def About(request):
    return HttpResponse("<h1>this is about page</h1>")

# show html template in this page
def HomeTemplate(request):
    return render(request, 'index.html')

#
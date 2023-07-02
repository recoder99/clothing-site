from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, "home/index.html")

def faq(request):
    return render(request, "home/faq.html")

def login(request):
    return render(request, "home/login.html")

def signup(request):
    return render(request, "home/signup.html")

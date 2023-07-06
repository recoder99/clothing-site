from django.shortcuts import render
from django.http import HttpResponse
from .forms import signup_form
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def homepage(request):
    return render(request, "home/index.html")

def faq(request):
    return render(request, "home/faq.html")

def login(request):
    return render(request, "home/login.html")

def signup(request):
    
    form = UserCreationForm()
    print("test_point_0")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("test_point_1")
        if form.is_valid():
            print("test_point_2")
            form.save()
    
    context = {}

    context['form'] =  form
    return render(request, "home/signup.html", context)

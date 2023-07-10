from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import signup_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import pi_form
from .models import *
from django.contrib import redirects
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):

    products = Product.objects.all()
    return render(request, "home/index.html", {"products": products})


def faq(request):
    return render(request, "home/faq.html")


def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if User is not None:
            if user.is_active:
                request.session.set_expiry(86400)  # sets the exp. value of the session
                login(request, user)
                return redirect("/")

    return render(request, "home/login.html")


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 != password2:
            return HttpResponse("password does not match")

        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect("/login")

    return render(request, "home/signup.html")


def product_page(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "home/product_page.html", {"product": product})


@login_required(login_url="login")
def add_to_cart(request):
    print("testpoint1")
    if request.method == "POST":
        product_id = request.POST["product_id"]
        quantity = int(request.POST["quantity"])
        print(product_id, quantity)

        product = Product.objects.get(pk=product_id)
        cart_item = Cart.objects.create(
            user_id=request.user, product_id=product, quantity=quantity, ordered=False
        )
        print(product)
        cart_item.save()
    return HttpResponse("")


@login_required
def cart(request):
    products = Cart.objects.filter(user_id=request.user, ordered=False)
    total = 0

    for price in products:
        total += price.product_id.price * price.quantity
    return render(request, "home/cart.html", {"products": products, "total": total})


@login_required
def update_cart(request):
    if request.method == "POST":
        print("debug1")
        str = request.POST["data"]
        data = str.split("_")
        print(data)
        p_id = int(data[1])
        cart_item = Cart.objects.get(pk=p_id)
        if data[0] == "inc":
            print("debug2")
            cart_item.quantity += 1
            cart_item.save()
        elif data[0] == "dec":
            cart_item.quantity -= 1
            cart_item.save()
    return HttpResponse("")


def information(request):
    return render(request, "home/information.html")

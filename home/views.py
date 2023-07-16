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
        PersonalInformation.objects.create(user_id=user)
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
        elif data[0] == "rm":
            cart_item.delete()
    return HttpResponse("")


@login_required(login_url="login")
def information(request):
    
    return render(
        request,
        "home/information.html",
        {"info": PersonalInformation.objects.get(user_id=request.user)},
        {"deliver", Orders.objects.get(user_id=request.user, delivered=False)},
        {"delivered", Orders.objects.get(user_id=request.user, delivered=True)}
    )


def edit_information(request):

    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        address_1 = request.POST["address_1"]
        city = request.POST["city"]
        province = request.POST["province"]
        zipcode = request.POST["zipcode"]

        contact_no = request.POST["contact_no"]

        user = User.objects.get(id=request.user.id)
        user_info = PersonalInformation.objects.get(user_id=request.user)

        user_info.address_1 = address_1
        user_info.city = city
        user_info.province = province
        user_info.zipcode = zipcode
        user_info.ContactNumber = contact_no
        user_info.save()

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

    return render(
        request,
        "home/edit_information.html",
        {"info": PersonalInformation.objects.get(user_id=request.user)},
    )


@login_required(login_url="login")
def checkout(request):
    cart_items = Cart.objects.filter(user_id=request.user)
    cart_items.filter()
    user_info = PersonalInformation.objects.get(user_id=request.user)

    if request.method == "POST":

        data = request.POST["pay_method"]
        address = "{0}, {1}, {2}, {3}".format(
            user_info.address_1, user_info.city, user_info.province, user_info.zipcode
        )
        order = Orders.objects.create(user_id=request.user, delivered=False, pay_method=data, delivery_address=address)
        user_info = PersonalInformation.objects.get(user_id=request.user)
        for i in cart_items:
            OrderDetails.objects.create(order_id=order, product_id=i.product_id, quantity=i.quantity)
            i.ordered = True
            i.product_id.sold += i.quantity
            i.save()
            i.product_id.save()

        cart_items.filter(ordered=True).all().delete()

    return render(request, "home/checkout.html", {"cart": cart_items, "info": user_info})

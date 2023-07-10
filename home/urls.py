from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home-page"),
    path("faq", views.faq, name="faq"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("signup", views.signup, name="signup"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("cart", views.cart, name="cart"),
    path("product/<int:id>", views.product_page, name="product_page"),
    path("update_cart", views.update_cart, name="update_cart"),
    path("information", views.information, name="information"),
    path("edit_information", views.edit_information, name="edit_information"),
    path("checkout", views.checkout, name="checkout"),
]

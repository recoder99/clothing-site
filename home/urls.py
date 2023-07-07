from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('faq', views.faq, name='faq'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('product_page', views.product_page, name='product-page')
]

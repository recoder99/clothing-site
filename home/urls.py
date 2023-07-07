from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('faq', views.faq, name='faq'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup, name='signup'),
    path('product/<int:id>', views.product_page, name='product_page')
]

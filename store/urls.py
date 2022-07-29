from django.contrib import admin
from django.urls import path
from .Views.home import Index
from .Views.signup import Signup
from .Views.login import Login, logout
from .Views.cart import Cart
from .Views.checkout import CheckOut
from .Views.orders import OrderView
from store.middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name= 'signup'),
    path('login',Login.as_view(), name= 'login'),
    path('logout',logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='Checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]
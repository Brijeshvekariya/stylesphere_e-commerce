from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('seller_register/', views.seller_register, name='seller_register'),
    path('logout/', views.logout, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('new_password/', views.new_password, name='new_password'),
    path('profile/', views.profile, name='profile'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('seller_addproduct/',views.seller_addproduct,name='seller_addproduct'),
    path('seller_viewproducts/',views.seller_viewproducts,name='seller_viewproducts'),
]
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views , adminster_valida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),          #普通用户注册
    path('login/', views.login),                #普通用户登录
    path('login_admin/', adminster_valida.login_admin), #超级管理员登录

    path('add_shop/', adminster_valida.manage_shop.add_shop), #添加商品
    path('del_shop/', adminster_valida.manage_shop.del_shop), #删除商品

    path('find_shoping/', views.find_shoping),    #查询商品
    path('upload/', adminster_valida.upload),     #上传文件
    
    path('all_orders/', adminster_valida.all_orders),     #所有订单列表


#公告管理 管理员
    path('add_announcement/', adminster_valida.Announcement.add_announcement),     #添加公告
    path('all_announcement/', adminster_valida.Announcement.all_announcement),     #所有公告
    path('del_announcement/', adminster_valida.Announcement.del_announcement),     #删除公告

#购物车管理 普通用户
    path('add_shop_car/', views.Shop_Cart.add_shop_car),    #添加一件商品到购物车
    path('all_shop_car/', views.Shop_Cart.all_shop_car),    #查询当前用户所有购物车内容
    path('del_shop_car/', views.Shop_Cart.del_shop_car),    #查询当前用户所有购物车内容

#订单管理 普通用户
    path('create_order/', views.create_order),    #新建订单
    
    
    
]
"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),# 反向解析 动态生成路径
    path('tinymce/', include('tinymce.urls')),  # 富文本编辑器
    path('search', include('haystack.urls')),  # 全文检索框架
    path('user/', include('user.urls')),  # 用户模块
    path('cart/', include('cart.urls')),  # 购物车模块
    path('order/', include('order.urls')),  # 订单模块
    path('', include('goods.urls')),  # 商品模块
]














"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myapp.md_uesr import *
from myapp.views import *
from myapp.kaoshi import *
from myapp.md_goods import *
# from myapp.tests_shangchuan import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('myapp1/',hello),
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
    path('code/',Mycode.as_view()),
    path('md_main/weibo/',wb_back),
    path('ding_url/',ding_url),
    path('upload/',UploadFile.as_view()),
    path('qiniu/',Qiniu.as_view()),
    path('ding_login/',ding_login),
    path('ding_back/',ding_back),
    path('upyun/',UPYUpload.as_view()),
    path('userinfo/',UserInfo.as_view()),
    path('getcarousel/',GetCarousel.as_view()),
    path('shop/',Shop.as_view()),
    path('insertgoods/',InsertGoods.as_view()),
    path('categorylist/',CategoryList.as_view()),
    path('goodslist/',GoodsList.as_view()),
    path('goodinfo/',GoodInfo.as_view()),
    path('imagelist/',ImageList.as_view()),
    path('search/',Search.as_view()),
    path('commentinsert/',CommentInsert.as_view()),
    path('commentlist/',CommentList.as_view()),

    # path('uploadfile/',Upload.as_view()),

]

"""python_web_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path

#from app01.views import index,login,publisher_list,add_publisher,delete_publisher,update_publisher
from app01.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('login/', login),
    path('publisher_list/', publisher_list),
    path('add_publisher/', add_publisher),
    path('delete_publisher/', delete_publisher),
    path('update_publisher/', update_publisher),

    path('book_list/', book_list),
    path('delete_book/', delete_book),
    path('add_book/', add_book),
    path('update_book/', update_book),

    path('author_list/', author_book),
    path('add_author/', add_author),
    path('delete_author/', delete_author),
    path('update_author/', update_author),

    path('upload_file/', UploadView.as_view()),
    path('json_data/', json_data),

    re_path(r'', publisher_list), #如果都没匹配上默认执行publisher_list

]

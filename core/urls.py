"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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


from main.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('searh/', PostsView.as_view(), name='search'),
    path('', PostsView.as_view(), name='main'),
    path('detail/<int:pk>/', PostsDetail.as_view(), name='detail'),
    path('create/', CreatePosts.as_view(), name='create'),
    path('update/<int:pk>/', UpdatePosts.as_view(), name='update'),
    path('delete/<int:pk>', delete_post, name='delete'),
    path('regiser/', UserCreateView.as_view(), name='register'),
    path('log_out/', log_out, name='log_out'),
    path('login/', user_login, name='login'),
]

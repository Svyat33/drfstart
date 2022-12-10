"""djangoProject2 URL Configuration

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

from frontend.views import news_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/news/', news_list),
    path('api/v1/news/<pk:news_id>', news_one),
]
'''
/api/v1/news/   - GET return all news 
/api/v1/news/3/ - GET one news 
/api/v1/news/   - POST create news
/api/v1/news/3/ - DELETE delete one news
'''
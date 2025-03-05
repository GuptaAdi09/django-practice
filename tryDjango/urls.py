"""
URL configuration for tryDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from .views import home
from polls.views import index


from articles.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register_user,name='register_user'),
    path('',article_with_htmlResponse,name='HTMLResponse'),
    path('login/',login_user,name="login_user"),
    path('logout/',logout_user,name="logout_user"),
    path('search_article/',search_article,name='search_article'),
    
    path('HttpResponseArticle/',article_with_HTTpResponse,name='HTTPResponse'),
    path('htmlResponseArticle/',article_with_htmlResponse,name='HTMLResponse'),
    # path('description/<int:id>/',description_view,name='description_view'),
    path('article/create/',create_articel,name='create_articel'),
    

    path('polls/',include('polls.urls')),
    path('politics/',include('Politics.urls')),
    
    
]

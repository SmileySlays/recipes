"""recipe_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from recipe_box.models import Author, Recipe
from recipe_box import views

admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="homepage"),
    path('myitem/<int:id>/', views.details),
    path('myauthor/<str:name>/', views.auth_deets),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('recipeedit/<pk>/', views.edit_recipe, name="recipeedit"),
    path("favorite/<pk>", views.favorite_add_view, name="favorite"),
]

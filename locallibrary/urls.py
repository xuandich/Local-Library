"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, re_path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('index/', views.index),

    path('book/', views.book),
    path('addbook/', views.addbook),
    path('book/<id>/delete', views.delbook),
    path('book/<id>/edit', views.editbook),
    path('book/<id>/bookdetail', views.bookdetail),

    path('author/', views.author),
    path('addauthor/', views.addauthor),
    path('editauthor/<id>', views.editauthor),
    path('delauthor/<id>', views.delauthor),
    path('author_book/<id>', views.author_book),

    path('category/', views.category),
    path('addcategory', views.addcategory),
    path('editcategory/<id>', views.editcategory),
    path('delcategory/<id>', views.delcategory),
    path('category_book/<id>', views.category_book),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/index/', permanent=True)),
    path('search/', views.search, name='search'),
]


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
    re_path(r"^book/(\d+)/delete", views.delbook),
    re_path(r"^book/(\d+)/edit", views.editbook),

    re_path(r'^author/', views.author),
    re_path(r'^addauthor', views.addauthor),
    re_path(r'^editauthor/(\d+)', views.delauthor),
    re_path(r'^delauthor/(\d+)', views.delauthor),
    re_path(r'^author_book/(\d+)', views.author_book),
]

from django.views.generic.base import TemplateView
urlpatterns += [
    path('', RedirectView.as_view(url='/index/', permanent=True)),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]


"""testDjango URL Configuration

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
import os

from django.urls import re_path, path

os.path.abspath(".")
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.hello),
    re_path(r"^$", views.hello, name="hello"),
    re_path(r"^hello/$", views.hello, name="hello"),
    re_path(r"^index/$", views.index, name="index"),
    path("runoob/", views.runoob),
    re_path(r"^base/$", views.base, name="base"),
]

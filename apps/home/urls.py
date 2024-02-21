# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path ('',views.home, name='home'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

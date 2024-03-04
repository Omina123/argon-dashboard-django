# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index', index, name='index'),
    path('homei', homei, name='homei'),

    path('login/', login_view, name="login_view"),
    path('register/', register_user, name="register_user"),

     path('enter', enter, name='enter'),
          path('get_reco', get_reco, name='get_reco'),
           path('fogot_password', fogot_password, name='fogot_password'),

     path('delete/<int:pk>', delete, name='delete'),
     path('hire/<int:pk>', hire, name='hire'),
            #    path('omina', omina, name='omina'),
path('pdf/<int:pk>', pdf, name='pdf'),
          path('kevo', kevo, name='kevo'),

          path('history', history, name='history'),

          
    path("logout/", LogoutView.as_view(), name="logout"),
    


    
]
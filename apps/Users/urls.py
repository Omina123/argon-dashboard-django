from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from Users import views

urlpatterns = [
    path('register_user',views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),

    path('logout/', LogoutView.as_view(next_page='login_user'), name='logout'),


    path('admin/', admin.site.urls),
     
]

from django.shortcuts import render
from .forms import*
# In your views.py
from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     form_class = LoginForm

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             return redirect('home')  # Replace 'home' with the actual URL name you want to redirect to upon successful login
#     else:
#         form = LoginForm()

#     return render(request, 'login.html', {'form': form})
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)
            
            if user.is_Student:
                login(request, user)
                return redirect('index') 
            if user.is_lecture:
                login(request,user)
                return redirect('home')
                # Replace 'home' with the actual URL name you want to redirect to upon successful login
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'form': form})


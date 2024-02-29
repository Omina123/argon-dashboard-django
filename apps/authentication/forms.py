# # -*- encoding: utf-8 -*-
# """
# Copyright (c) 2019 - present AppSeed.us
# """
# from .models import CustomUser

# from django import forms
# from django.contrib.auth.forms import UserCreationForm


# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Username",
#                 "class": "form-control"
#             }
#         ))
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password",
#                 "class": "form-control"
#             }
#         ))


# class  SignUpForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
    
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email','password', 'role']


# # class SignUpForm(UserCreationForm):
# #     username = forms.CharField(
# #         widget=forms.TextInput(
# #             attrs={
# #                 "placeholder": "Username",
# #                 "class": "form-control"
# #             }
# #         ))
# #     email = forms.EmailField(
# #         widget=forms.EmailInput(
# #             attrs={
# #                 "placeholder": "Email",
# #                 "class": "form-control"
# #             }
# #         ))
# #     password1 = forms.CharField(
# #         widget=forms.PasswordInput(
# #             attrs={
# #                 "placeholder": "Password",
# #                 "class": "form-control"
# #             }
# #         ))
# #     password2 = forms.CharField(
# #         widget=forms.PasswordInput(
# #             attrs={
# #                 "placeholder": "Password check",
# #                 "class": "form-control"
# #             }
# #         ))

# #     class Meta:
# #         model = User
# #         fields = ('username', 'email', 'password1', 'password2')
# users/forms.py
from .models import*

# class SymptomForm(forms.ModelForm):
#     class Meta:
#         model = AnthraxSymptom
#         fields = '__all__'
# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class YourForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        help_text='',
        label='',  # Set label to an empty string to remove it
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    # other form fields...

    def __init__(self, *args, **kwargs):
        super(YourForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Register'))

class SymptomForm(forms.Form):
    symptoms = forms.CharField(widget=forms.Textarea, label=' Enter Symptoms')
    
class ApproveUserForm(forms.ModelForm):
    class Meta:
        model=AnthraxSymptom
        fields=['farmer']
        Widget={
        'farmer': forms.TextInput(attrs={'class':'form-control','placeholder': 'username'})

        }



class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email',  'first_name', 'last_name','role')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Hash the password
        if commit:
            user.save()
        return user
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
class FogotForm(forms.Form):
    email= forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    # password = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Enter new password",
    #             "class": "form-control"
    #         }
    #     ))
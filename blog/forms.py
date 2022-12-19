from django import forms
from django.db import models
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content','photo','is_published','category']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-input'})
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
       model=Category
       fields=['name','slug']

       widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'})
        }

class RegisterUserForm(UserCreationForm):
    username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    biography=forms.CharField(label="Расскажите о себе",widget=forms.Textarea(attrs={'class':'form-input'}))
    avatar=forms.ImageField(label='Ваша фотография', widget=forms.FileInput(attrs={'class':'user-photo'}))
    class Meta():
        model= CustomUser
        fields= ('username', 'password1','password2','biography','avatar')

class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
   
    class Meta:
        model=CustomUser
        fields=['username', 'password']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=['text']
        widgets={
            'text':forms.Textarea(attrs={'class':'form-input'})
        }
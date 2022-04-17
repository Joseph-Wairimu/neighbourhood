from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,NeighborHood,Business,Post


class RegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= User
        fields=["username","email","password1","password2"]        


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=["name","email","location","profile_pic","neighborhood"]

class NeighborHoodForm(forms.ModelForm):
    class Meta:
        model= NeighborHood
        fields=["image","name","location","occupants_count"]       

class BusinessForm(forms.ModelForm):
    class Meta:
        model= Business
        fields=["name","location","neighborhood","email","profile_pic"]        

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=["title","description","image","hood"]
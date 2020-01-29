from django import forms
from .models import *


class MovieForm(forms.Form):
    title=forms.CharField(label='Title',max_length=200, required=True)
    duration=forms.IntegerField(label='Duration', required=True)
    description=forms.CharField(label='Description', required=True)
    image=forms.ImageField(label='Picture', required=True)

class LoginForm(forms.Form):
    loginClass=forms.TextInput(attrs={'class' : 'form-control'})
    passwordClass=forms.PasswordInput(attrs={'class' : 'form-control'})
    login=forms.CharField(widget=loginClass, label="Login", max_length=50, required=True)
    password=forms.CharField(widget=passwordClass, label="Password", max_length=50, required=True)


class RegisterForm(forms.Form):
    txtClass=forms.TextInput(attrs={'class':'form-control'})
    passwordClass=forms.PasswordInput(attrs={'class':'form-control'})
    login=forms.CharField(widget=txtClass, label="Login", max_length=50, required=True)
    email=forms.CharField(widget=txtClass, label="Email", max_length=50, required=True)
    password=forms.CharField(widget=passwordClass, label="Password", max_length=50, required=True)

class TicketForm(forms.Form):
    tickets=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Ticks")

class OrderForm(forms.Form):
    delete=forms.CharField()
    submit=forms.CharField()
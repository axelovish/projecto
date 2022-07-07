from django import forms
from .models import Libro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields ='__all__'

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1: forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password1: forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}        

from django import forms

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

        widgets = {
            "username": forms.TextInput(attrs={'placeholder': "nom", 'class': 'form-control'}),
            "email": forms.TextInput(attrs={'placeholder': "Ex: bakole@monalina.com", 'class': 'form-control'}),
            "password": forms.PasswordInput(attrs={'placeholder': "*********", 'class': 'form-control'}),
            "role": forms.Select(attrs={'class': 'form-control'})
        }


class LoginForm(forms.Form):
    identifier = forms.CharField(
        label="Identifiant",
        widget=forms.TextInput(attrs=({
            'placeholder': 'nom ou email',
        })),
        error_messages={
            'required': 'Ce champ est réquis.'
        }
    )

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'placeholder': '************',
        }),
        error_messages={
            'required': 'Ce champ est réquis.'
        }
    )
from django import forms


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
from django import forms
from .models import Account, Prospect, Opportunity

from dealflow.lib.url_parse import is_valid_url_structure


class AccountForm(forms.ModelForm):
    
    class Meta:
        model = Account
        exclude = ['user', 'status']
        fields = "__all__"

        widgets = {
            "account_name": forms.TextInput(attrs={'placeholder': "nom de l'entreprise", 'class': 'form-control'}),
            "address": forms.TextInput(attrs={'placeholder': "address", 'class': 'form-control'}),
            "activity_sector": forms.TextInput(attrs={'placeholder': "secteur d'activité", 'class': 'form-control'}),
            "description": forms.Textarea(attrs={'placeholder': "description", 'class': 'form-control'}),
            "account_phone_number": forms.TextInput(attrs={'placeholder': "Ex: +243 92 524 463 3", 'class': 'form-control'}),
            "web_site": forms.TextInput(attrs={'placeholder': "Ex: https://exemple.com", 'class': 'form-control'}),
            "postal_code": forms.TextInput(attrs={'placeholder': "code postal", 'class': 'form-control'}),
        }

    def clean_web_site(self):
        url = self.cleaned_data.get("web_site")

        if not is_valid_url_structure(url):
            return forms.ValidationError("URL est invalide")
        
        return url

class ProspectForm(forms.ModelForm):
    
    class Meta:
        model = Prospect
        exclude = ['user', 'account', 'status']
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': "nom", 'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'placeholder': "post-nom", 'class': 'form-control'}),
            "post_title": forms.TextInput(attrs={'placeholder': "titre de post", 'class': 'form-control'}),
            "email": forms.TextInput(attrs={'placeholder': "Ex: bakole@monalina.com", 'class': 'form-control'}),
            "phone_number": forms.TextInput(attrs={'placeholder': "Ex: +243 92 524 463 3", 'class': 'form-control'})
        }


class OpportunityForm(forms.ModelForm):
    
    class Meta:
        model = Opportunity
        exclude = ['user', 'account', 'pipeline']
        fields = "__all__"

        widgets = {
            "deal_name": forms.TextInput(attrs={'placeholder': "nom de l'affaire", "class": "form-control"}),
            "estimate_value": forms.TextInput(attrs={'placeholder': "valeur estimée", "class": "form-control"}),
            "cloture_date": forms.DateTimeInput(attrs={'placeholder': "Ex: 2025-04-02 12:44", "class": "form-control"}),
            "probability_purcent": forms.TextInput(attrs={'placeholder': "pourcentage de probalité", "class": "form-control"})
        }


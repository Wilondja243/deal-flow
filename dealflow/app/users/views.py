from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import LoginForm, UserForm


class SignupView(LoginRequiredMixin, View):
    form_class = UserForm
    template_name = "crm/create_user.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        
        if request.method == "POST":
            form = self.form_class(request.POST)

            if form.is_valid():
                user = User(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    role=form.cleaned_data['role']
                )
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, "Utilisateur crée avec success.")
                return redirect("dashboard")
        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = "users/login.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            passowrd = form.cleaned_data['password']

            user = authenticate(request, username=identifier, password=passowrd)

            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard'))
            else:
                messages.error(request, "Identifiant incorrect")
        return render(request, self.template_name, {'form': form})
    

class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))
            

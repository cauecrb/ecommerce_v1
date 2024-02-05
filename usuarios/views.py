from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
import copy

from . import models
from . import forms


class BaseUsusarios(View):
    
    template_name = 'usuarios/criar.html'
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        self.carrinho = copy.deepcopy(self.request.get('carrinho', {}))
        
        self.usuarios = None
                
        if self.request.user.is_authenticated:
            self.usuarios = models.Usuario.objects.filter(
                usuario=self.request.user
            ).first()
            
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                ),
                'usuariosform': forms.UsuariosForm(data=self.request.POST or None)
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(data=self.request.POST or None),
                'usuariosform': forms.UsuariosForm(data=self.request.POST or None)
            }
        
        self.userform = self.contexto['userform']
        self.usuariosform = self.contexto['usuariosform']
        
        
        self.renderizar = render(self.request, self.template_name, self.contexto)
    
    def get(self, *args, **kwargs):
        return self.renderizar


class Criar(BaseUsusarios):
    def post(self, *args, **kwargs):
        #if not self.userform.is_valid() or not self.usuariosform.is_valid():
        if not self.userform.is_valid():
            print('Invalido')
            return self.renderizar
        
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        #usuario logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username)
            
            usuario.username = username
            
            if password:
                usuario.set_password(password)
            
            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()
        
        #usuario não logado
        else:
            pass
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()
            
            perfil = self.userform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
        
        self.request.session['carrinho'] = self.carrinho
        self.request.session.save()
        
        return self.renderizar


class Atualizar(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('atualizar')

class Login(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('login')

class Logout(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('logout')

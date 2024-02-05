from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

from . import models
from . import forms


class BaseUsusarios(View):
    
    template_name = 'usuarios/criar.html'
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
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
        if not self.userform.is_valid() or not self.usuariosform.is_valid():
            print('Invalido')
            return self.renderizar
        if self.request.user.is_authenticated:
            pass
        else:
            pass
            
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

from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class Criar(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('pagar')

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

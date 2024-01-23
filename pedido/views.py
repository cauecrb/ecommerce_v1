from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse



class Pagar(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('pagar')

class FecharPedido(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('fechar pedido')

class Detalhe(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('detalhe')

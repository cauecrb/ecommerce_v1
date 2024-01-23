from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models



class ListaProdutos(ListView):
    #pass
    """def get(self, *args, **kwargs):
        return HttpResponse('lista produto')"""
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10

class DetalheProdutos(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('detalhe produto')

class AdicionarProduto(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('adicionar produto')

class RemoverProduto(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('remover produto')

class Carrinho(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('carrinho')

class Finalizar(View):
    #pass
    def get(self, *args, **kwargs):
        return HttpResponse('finalizar')

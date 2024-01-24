from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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

class DetalheProdutos(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


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

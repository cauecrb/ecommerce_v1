from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
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
    def get(self, *args, **kwargs):
        #http_referer = self.request.META['HTTP_REFERER']
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')
        
        if not variacao_id:
            messages.error(
                self.request, 'Produto Inexistente'
            )
            return redirect(http_referer)
        
        variacao = get_object_or_404(models.Variacao, pk=variacao_id)
        # TODO: redirecionar caso 404
        
        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()
        
        carrinho = self.request.session['carrinho']
        
        if variacao_id in carrinho:
            # TODO: Variação existe no carrinho
            pass
        else:
            # TODO: Variação não existe no carrinho
            pass
        
        return HttpResponse(f'{variacao.produto} {variacao.nome}')

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

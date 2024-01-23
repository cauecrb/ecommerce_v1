from django.urls import path
from . import views


app_name = 'produto'  #produto:detalhe

urlpatterns = [
    path('', views.ListaProduto.as_view(), name="lista"),
    path('<slug>', views.DetalheProduto.as_view(), name="detalhe"),
    path('adicionar/', views.AdicionarProduto.as_view(), name="adicionar"),
    path('remover/', views.RemoverProduto.as_view(), name="remover"),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho"),
    path('finalizar/', views.Finalizar.as_view(), name="finalizar"),


]

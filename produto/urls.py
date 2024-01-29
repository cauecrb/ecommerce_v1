from django.urls import path
from . import views


app_name = 'produto'  #produto:detalhe

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProdutos.as_view(), name="detalhe"),
    path('adicionar/', views.AdicionarProduto.as_view(), name="adicionar"),
    path('remover/', views.RemoverProduto.as_view(), name="remover"),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho"),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name="resumodacompra"),


]

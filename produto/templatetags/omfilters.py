from django.template import Library
from utils import utils


register = Library()


@register.filter
def formata_preco(val):
    return utils.formata_preco(val)

@register.filter
def carr_total_qtd(carrinho):
    return utils.carr_total_qtd(carrinho)

@register.filter
def carr_total_val(carrinho):
    return utils.carr_total_val(carrinho)
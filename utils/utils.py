def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.',',')

def carr_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])

def carr_total_val(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if  item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item 
            in carrinho.values()
        ]
    )
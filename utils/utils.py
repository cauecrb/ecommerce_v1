def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.',',')

def carr_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])
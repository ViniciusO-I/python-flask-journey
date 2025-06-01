# Descrições dos produtos da loja
descricao_lovely_loveseat = """Lovely Loveseat. Tecido de poliéster com madeira. 
Altura: 32 pol, Largura: 40 pol, Profundidade: 30 pol. Disponível nas cores vermelha ou branca.
"""

preco_lovely_loveseat = 254.00

descricao_sofa_estiloso = """Stylish Settee. Couro sintético sobre madeira de bétula. 
Altura: 29.50 pol, Largura: 54.75 pol, Profundidade: 28 pol. Cor: Preto.
"""

preco_sofa_estiloso = 180.50

descricao_luminaria_luxuosa = """Luxurious Lamp. Vidro e ferro. 
Altura: 36 pol. Cor: Marrom com cúpula creme.
"""

preco_luminaria_luxuosa = 52.15

# Taxa de imposto sobre vendas (8.8%)
taxa_imposto = 0.088

# Total gasto pelo Cliente 1 até agora
total_cliente_um = 0

# Itens que o cliente comprou (descrições)
itens_cliente_um = ""

# Cliente 1 comprou o Lovely Loveseat
total_cliente_um += preco_lovely_loveseat
itens_cliente_um = descricao_lovely_loveseat

# Cliente 1 também comprou a Luminária Luxuosa
total_cliente_um += preco_luminaria_luxuosa
itens_cliente_um += descricao_luminaria_luxuosa

# Cálculo do imposto sobre o total atual
imposto_cliente_um = total_cliente_um * taxa_imposto
total_cliente_um += imposto_cliente_um

# Impressão do recibo
print("Itens do Cliente 1:")
print(itens_cliente_um)
print("Total do Cliente 1: R$", round(total_cliente_um, 2))

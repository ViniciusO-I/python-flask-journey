import random

# Nome do usuario e pergunta
nome = "Coloque um nome de entrada"
pergunta = "Coloque uma pergunta de entrada"
resposta = ""

# Gera um numero aleatorio entre 1 e 9
numero_aleatorio = random.randint(1, 9)

# Define a resposta com base no numero
if numero_aleatorio == 1:
    resposta = "Sim - definitivamente"
elif numero_aleatorio == 2:
    resposta = "Com certeza"
elif numero_aleatorio == 3:
    resposta = "Sem duvida"
elif numero_aleatorio == 4:
    resposta = "Resposta confusa, tente novamente"
elif numero_aleatorio == 5:
    resposta = "Pergunte novamente mais tarde"
elif numero_aleatorio == 6:
    resposta = "Melhor nao te contar agora"
elif numero_aleatorio == 7:
    resposta = "Minhas fontes dizem que nao"
elif numero_aleatorio == 8:
    resposta = "Perspectiva nao muito boa"
elif numero_aleatorio == 9:
    resposta = "Muito improvavel"
else:
    resposta = "Erro: numero fora do intervalo"

# Exibe a resposta formatada
print(f"{nome} pergunta: {pergunta}")
print(f"Resposta da Bola Magica: {resposta}")
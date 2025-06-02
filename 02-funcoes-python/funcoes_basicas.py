# Funcoes basicas para planejamento de viagem

# Funcao que exibe mensagem de boas-vindas ao usuario
def saudacao_planejador_viagem(nome): 
    print("Bem-vindo ao Planejador de Viagem v1.0, " + nome)

# Chamando a funcao de saudacao
saudacao_planejador_viagem("Vinicius")

# Funcao que arredonda o tempo estimado para o inteiro mais proximo
def tempo_estimado_arredondado(tempo_estimado):
    tempo_arredondado = round(tempo_estimado)
    return tempo_arredondado

# Armazenando a estimativa arredondada
estimativa = tempo_estimado_arredondado(72.5)

# Funcao que exibe o plano da viagem
def configurar_destino(origem, destino, tempo_estimado, meio_de_transporte="Carro"):
    print("Sua viagem comeca em " + origem)
    print("Voce esta viajando para " + destino)
    print("Voce viajara de " + meio_de_transporte)
    print("A viagem levara aproximadamente " + str(tempo_estimado) + " horas")

# Chamando a funcao com os dados do exemplo
configurar_destino("Sao Paulo", "Bahia", estimativa, "Carro")
# Funcao para converter temperatura de Fahrenheit para Celsius

def fahrenheit_para_celsius(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

# Exemplo de uso
temp_celsius = fahrenheit_para_celsius(100)
print("Temperatura em Celsius:", round(temp_celsius, 2))


# Funcao para calcular a forca (F = massa * aceleracao)

def calcular_forca(massa, aceleracao):
    return massa * aceleracao

# Dados do trem
massa_trem = 22680
aceleracao_trem = 10

# Resultado da forca
forca_trem = calcular_forca(massa_trem, aceleracao_trem)
print("A forca do trem e:", forca_trem)


# Funcao para calcular energia (E = m * c^2)

def calcular_energia(massa, c = 3 * 10**8):
    return massa * c**2

massa_bomba = 1
energia_bomba = calcular_energia(massa_bomba)
print("A energia da bomba e:", energia_bomba)

# Reutilizando a funcao de forca
def calcular_forca(massa, aceleracao):
    return massa * aceleracao

# Funcao para calcular trabalho (Work = Forca * Distancia)

def calcular_trabalho(massa, aceleracao, distancia):
    forca = calcular_forca(massa, aceleracao)
    trabalho = forca * distancia
    return trabalho

# Dados
massa_trem = 22680
aceleracao_trem = 10
distancia_trem = 100

# Calculo do trabalho
trabalho_trem = calcular_trabalho(massa_trem, aceleracao_trem, distancia_trem)

print(f"O trem GE realiza {trabalho_trem} Joules de trabalho ao percorrer {distancia_trem} metros.")

# Usando lambda para calcular quadrado de cada numero
numeros = [2, 4, 6, 8]
quadrados = list(map(lambda x: x**2, numeros))

print("Lista original:", numeros)
print("Quadrados:", quadrados)

# Usando lambda para converter lista de Fahrenheit para Celsius
fahrenheit = [32, 100, 212]
celsius = list(map(lambda f: (f - 32) * 5 / 9, fahrenheit))

print("Temperaturas em Fahrenheit:", fahrenheit)
print("Convertidas para Celsius:", celsius)
class Estudante:
  def __init__(self, nome, ano):
    self.nome = nome
    self.ano = ano
    self.notas = []

  def adicionar_nota(self, nota):
    if type(nota) is Nota:
      self.notas.append(nota)

class Nota:
  nota_minima = 65

  def __init__(self, valor):
    self.valor = valor

joao = Estudante("Joao", 10)
maria = Estudante("Maria", 12)
jose = Estudante("Jose", 8)

jose.adicionar_nota(Nota(100))
joao.adicionar_nota(Nota(20))
maria.adicionar_nota(Nota(30))
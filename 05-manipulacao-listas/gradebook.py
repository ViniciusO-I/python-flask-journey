# Boletim do semestre anterior
last_semester_gradebook = [
    ["politics", 80],
    ["latin", 96],
    ["dance", 97],
    ["architecture", 65]
]

# Novas materias e notas
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Criacao do novo boletim
gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]

# Adicionando novas materias
gradebook.append(["computer_science", 100])
gradebook.append(["visual_arts", 93])

# Atualizando nota de visual arts
gradebook[-1][-1] = 98

# Removendo nota da materia poetry
gradebook[2].remove(85)

# Adicionando status 'Pass' para poetry
gradebook[2].append("Pass")

# Removendo nome da materia poetry (apenas demonstracao)
gradebook[2].remove("poetry")

# Concatenando boletim anterior com o novo
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
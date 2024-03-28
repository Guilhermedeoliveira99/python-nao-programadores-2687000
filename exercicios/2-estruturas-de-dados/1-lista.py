# Crie uma lista apenas com elementos numéricos
anos = [2000, 2001, 2003, 2004]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
pessoas = ['Guilherme', 22, 2002, ['excel', 'PPT', 'Word'], True, ['fut', 'musica', 'assistir'], False]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(pessoas[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(pessoas[0:-1:2])

# Remova da lista o último item
print(pessoas.pop())

# Insira na lista um novo item
(pessoas.append('28'))
print(pessoas)

# Remova da lista um item específico
pessoas.remove(2002)
print(pessoas)

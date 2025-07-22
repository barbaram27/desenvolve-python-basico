# Solicita as duas listas ao usuário
entrada1 = input("Digite os números da primeira lista separados por espaço: ")
entrada2 = input("Digite os números da segunda lista separados por espaço: ")

# Converte as entradas em listas de inteiros
lista1 = [int(num) for num in entrada1.split()]
lista2 = [int(num) for num in entrada2.split()]

# Lista combinada alternadamente
lista_intercalada = []

# Descobre o tamanho da maior lista
max_len = max(len(lista1), len(lista2))

# Intercala os elementos
for i in range(max_len):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])

# Exibe a nova lista
print("Lista intercalada:", lista_intercalada)

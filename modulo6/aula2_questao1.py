import random

# Gera 20 valores inteiros entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Lista ordenada sem modificar a original
lista_ordenada = sorted(lista)

# Índice do maior e menor valor
indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

# Impressão dos resultados
print("=== ATIVIDADE 1 ===")
print("Lista ordenada (sem alterar a original):", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
print()

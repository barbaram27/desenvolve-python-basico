import random
from collections import Counter

# Gera duas listas com 20 inteiros entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Interseção ordenada, sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

# Conta quantas vezes cada elemento aparece em cada lista
contador1 = Counter(lista1)
contador2 = Counter(lista2)

# Impressão dos resultados
print("=== ATIVIDADE 3 ===")
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção (sem duplicatas e ordenada):", interseccao)

print("\nContagem em lista1:")
for elem in interseccao:
    print(f"{elem}: {contador1[elem]} vez(es)")

print("\nContagem em lista2:")
for elem in interseccao:
    print(f"{elem}: {contador2[elem]} vez(es)")


import random  # <- IMPORTANTE!

# Gera um valor aleatório entre 5 e 20
num_elementos = random.randint(5, 20)

# Cria a lista com valores entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcula soma e média
soma = sum(elementos)
media = soma / num_elementos

# Impressão dos resultados
print("=== ATIVIDADE 2 ===")
print("Número de elementos:", num_elementos)
print("Lista de elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", media)

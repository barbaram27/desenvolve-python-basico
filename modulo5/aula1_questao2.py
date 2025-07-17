import random
import math

# Solicita ao usuário a quantidade de números
n = int(input("Digite a quantidade de números a serem gerados: "))

soma = 0

# Gera n valores aleatórios entre 0 e 100 e soma
for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor

# Calcula a raiz quadrada da soma
raiz = math.sqrt(soma)

# Exibe o resultado
print("Soma dos valores gerados:", soma)
print("Raiz quadrada da soma:", round(raiz, 2))
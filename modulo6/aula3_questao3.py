

import random

# Gera a lista aleatória
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Função para achar o intervalo com maior quantidade de negativos
def intervalo_mais_negativos(lst):
    max_neg = 0
    inicio_max = 0
    fim_max = 0

    # Verificar todos os intervalos possíveis
    for i in range(len(lst)):
        negativos = 0
        for j in range(i, len(lst)):
            if lst[j] < 0:
                negativos += 1
            # Se esta janela tem mais negativos, atualizar
            if negativos > max_neg:
                max_neg = negativos
                inicio_max = i
                fim_max = j

    return inicio_max, fim_max

inicio, fim = intervalo_mais_negativos(lista)

# Deletar o intervalo com maior quantidade de negativos
del lista[inicio:fim+1]

print("Editada:", lista)

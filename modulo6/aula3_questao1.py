
# Solicita ao usuário pelo menos 4 números inteiros
numeros = []

print("Digite pelo menos 4 números inteiros (aperte Enter sem digitar para encerrar):")

while True:
    entrada = input(f"Digite o {len(numeros)+1}º número: ")
    if entrada == '':
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, digite pelo menos 4 números.")
            continue
    try:
        num = int(entrada)
        numeros.append(num)
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

# Impressão com fatiamento
print("\nLista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[0::2])
print("Elementos de índice ímpar:", numeros[1::2])

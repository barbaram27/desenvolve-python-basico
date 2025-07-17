# Solicita dois números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Soma os números
soma = numero1 + numero2

# Verifica se a soma é par ou ímpar usando o operador %
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")

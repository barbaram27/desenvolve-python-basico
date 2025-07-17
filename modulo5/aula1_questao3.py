import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

while True:
    palpite = int(input("Tente adivinhar o número entre 1 e 10: "))

    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Parabéns! Você acertou!")
        break


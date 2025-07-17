# Solicita a avaliação do filme
avaliacao = int(input("Avalie o filme de 1 a 5: "))

# Verifica e imprime a mensagem conforme a nota
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Digite um número de 1 a 5.")

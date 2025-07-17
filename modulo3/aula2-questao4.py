# Solicita a classe do personagem
classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ").lower()

# Solicita os pontos de força
forca = int(input("Digite os pontos de força: "))

# Solicita os pontos de magia
magia = int(input("Digite os pontos de magia: "))

# Verifica se os atributos são consistentes com a classe escolhida
if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    valido = forca > 5 and forca <= 15 and magia > 5 and magia <= 15
else:
    valido = False  # Classe inválida

# Imprime o resultado
print(valido)

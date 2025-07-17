# Solicita dois números decimais ao usuário
num1 = float(input("Digite o primeiro número decimal: "))
num2 = float(input("Digite o segundo número decimal: "))

# Calcula a diferença absoluta e arredonda para 2 casas decimais
diferenca = round(abs(num1 - num2), 2)

# Exibe o resultado
print("A diferença absoluta é:", diferenca)


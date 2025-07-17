# Solicita o gênero
genero = input("Digite seu gênero (M ou F): ").upper()

# Solicita a idade
idade = int(input("Digite sua idade: "))

# Solicita o tempo de serviço
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Verifica se pode se aposentar com base nas regras
pode_aposentar = (
    (genero == "F" and idade > 60) or
    (genero == "M" and idade > 65) or
    (tempo_servico >= 30) or
    (idade >= 60 and tempo_servico >= 25)
)

# Imprime o resultado
print(pode_aposentar)

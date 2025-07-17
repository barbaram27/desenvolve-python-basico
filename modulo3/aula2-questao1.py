# entrada de dados
# idade de juliana
# idade de cris
idade_juliana = int (input())
idade_cris = int(input())

# processamento
# true se ambos foram maior de idade
# <exp1> juliana é maior de idade
# <exp2> cris é maior de idade
# <exp1> and <exp2>
# false em qualquer outro caso
pode_entrar = idade_juliana > 17 and idade_cris > 17

# saida
print(pode_entrar)
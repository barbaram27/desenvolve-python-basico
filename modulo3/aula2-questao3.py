# Pergunta a idade
idade = int(input("Qual a sua idade? "))

# Pergunta se já jogou pelo menos 3 jogos de tabuleiro (True ou False)
ja_jogou_3_jogos = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True ou False) ") == "True"

# Pergunta quantas vezes venceu um jogo
vitorias = int(input("Quantas vezes você já venceu um jogo de tabuleiro? "))

# Verifica se pode entrar no clube
pode_entrar = (16 <= idade <= 18) and ja_jogou_3_jogos and vitorias >= 1

# Imprime o resultado
print(pode_entrar)

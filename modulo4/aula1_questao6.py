N = int(input())

total = 0
total_coelho = 0
total_rato = 0
total_sapo = 0

for _ in range(N):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)

    total += quantidade

    if tipo == 'C':
        total_coelho += quantidade
    elif tipo == 'R':
        total_rato += quantidade
    elif tipo == 'S':
        total_sapo += quantidade

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_coelho}")
print(f"Total de ratos: {total_rato}")
print(f"Total de sapos: {total_sapo}")
print(f"Percentual de coelhos: {total_coelho / total * 100:.2f} %")
print(f"Percentual de ratos: {total_rato / total * 100:.2f} %")
print(f"Percentual de sapos: {total_sapo / total * 100:.2f} %")


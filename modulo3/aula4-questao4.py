try:
    distancia = float(input("Digite a distância da entrega (em km): ").replace(",", "."))
    peso = float(input("Digite o peso do pacote (em kg): ").replace(",", "."))

    # Define o preço por kg baseado na distância
    if distancia <= 100:
        preco_por_kg = 1.00
    elif distancia <= 300:
        preco_por_kg = 1.50
    else:
        preco_por_kg = 2.00

    # Calcula o valor do frete
    frete = peso * preco_por_kg

    # Se peso for maior que 10kg, acrescenta R$10
    if peso > 10:
        frete += 10

    print(f"Valor do frete: R${frete:.2f}")

except ValueError:
    print("Por favor, digite apenas números válidos para distância e peso.")

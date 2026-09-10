soma = 0
positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))

    soma += numero

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

media = soma / 10

print("\n--- RELATÓRIO ESTATÍSTICO ---")
print("Soma:", soma)
print("Quantidade de positivos:", positivos)
print("Quantidade de negativos:", negativos)
print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
print("Média: {:.2f}".format(media))
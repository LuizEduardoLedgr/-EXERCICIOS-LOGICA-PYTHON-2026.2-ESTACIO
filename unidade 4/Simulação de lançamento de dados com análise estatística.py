import random

# Parte 1 - Lançamento único
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

soma = dado1 + dado2

print("Primeiro dado:", dado1)
print("Segundo dado:", dado2)
print("Soma:", soma)

# Parte 2 - 10 lançamentos
contador = 0

for i in range(10):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    soma = dado1 + dado2

    print("Lançamento", i + 1)
    print("Dado 1:", dado1)
    print("Dado 2:", dado2)
    print("Soma:", soma)

    if soma == 7:
        contador += 1

print("A soma dos dados foi igual a 7:", contador, "vezes")
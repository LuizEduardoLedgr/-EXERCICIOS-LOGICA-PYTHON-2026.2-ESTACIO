import math

numero = float(input("Digite um número real: "))

print("Raiz quadrada:", math.sqrt(numero))
print("Valor absoluto:", math.fabs(numero))
print("Arredondamento para cima:", math.ceil(numero))
print("Arredondamento para baixo:", math.floor(numero))

if numero.is_integer() and numero >= 0:
    print("Fatorial:", math.factorial(int(numero)))
else:
    print("Fatorial: não é possível calcular. O número deve ser inteiro e não negativo.")
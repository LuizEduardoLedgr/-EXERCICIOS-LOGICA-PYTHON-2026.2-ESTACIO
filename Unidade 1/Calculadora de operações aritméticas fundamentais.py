A = float(input("digite o primeiro número: "))
B = float(input("digite o segundo número: "))
print("-------Os Resultados São-------")
print("soma:", A + B)
print("subtração:", A - B)
print("multiplicação:", A * B)
print("potenciação:", A ** B)
if B == 0:
    print("divisão por 0, não é permitida")
else:
    print("divisão:", A / B)
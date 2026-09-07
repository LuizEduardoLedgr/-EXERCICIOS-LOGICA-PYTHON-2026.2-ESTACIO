A = input("digite seu nome completo: ")
B = int(input("digite a sua idade:"))
while B < 0:
    print("a idade não pode ser negativa")
C = float(input("digite a sua altura: "))
while C <= 0:
    print("A altura deve ser maior que zero!")
D = input("digite onde você reside:")
print("ola, meu nome é", A, "tenho", B, "anos, minha altura é", C, "metros e moro em", D)
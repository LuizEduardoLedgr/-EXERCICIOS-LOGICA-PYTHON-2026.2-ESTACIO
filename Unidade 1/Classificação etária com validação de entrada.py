A = int(input("DIgite sua idade: "))
if A <= 12:
    print("Voc~e é uma criança")
elif A >= 13 and A <= 17:
    print("VOcê é um adolescente")
elif A >= 18 and A <= 59:
    print("Você é adulto")
else:
    print("Você é idoso")
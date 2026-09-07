A = float(input("digite sua primeira nota:"))
B = float(input("digite sua segunda nota:"))
C = float(input("digite sua terceira nota:"))
nota_final = (A + B + C) / 3
print(nota_final)
if nota_final >= 7:
    print("parabens, você esta aprovado")
elif nota_final <= 6.9:
    print("recuperação")
else:
    print("reprovado")
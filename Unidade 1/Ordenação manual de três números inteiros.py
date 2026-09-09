A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))
if A > B > C:
    print("A ordem crescente é :", A, B, C)
elif A > C > B:
    print("A ordem crescente é :", A, C, B)
elif B > A > C:
    print("A ordem crescente é :", B, A, C)
elif B > C > A:
    print("A ordem crescente é :", B, C, A)
elif C > A > B:
    print("A ordem crescente é :", C, A, B)
elif C > B > A:
    print("A ordem crescente é :", C, B, A)
numeros = []

while True:
    print('================================')
    print('GERENCIAMENTO DE NÚMEROS')
    print('================================')
    print('1 - Cadastrar número')
    print('2 - Listar números')
    print('3 - Exibir maior número')
    print('4 - Exibir menor número')
    print('5 - Calcular média')
    print('0 - Encerrar programa')
    
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        numero = float(input('Digite um número: '))
        numeros.append(numero)
        print('Número cadastrado!')

    elif opcao == 2:
        if len(numeros) == 0:
            print('Nenhum número cadastrado.')
        else:
            for numero in numeros:
                print(numero)

    elif opcao == 3:
        if len(numeros) == 0:
            print('Nenhum número cadastrado.')
        else:
            print('Maior número:', max(numeros))

    elif opcao == 4:
        if len(numeros) == 0:
            print('Nenhum número cadastrado.')
        else:
            print('Menor número:', min(numeros))

    elif opcao == 5:
        if len(numeros) == 0:
            print('Nenhum número cadastrado.')
        else:
            media = sum(numeros) / len(numeros)
            print(f'Média: {media:.2f}')

    elif opcao == 0:
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida.')
estudantes = []

# Tupla com as situações possíveis
situacoes = ("Aprovado", "Recuperação", "Reprovado")


def calcular_media(notas):
    return sum(notas) / len(notas)


def calcular_situacao(media):
    if media >= 7:
        return situacoes[0]
    elif media >= 5:
        return situacoes[1]
    else:
        return situacoes[2]


def cadastrar_estudante():
    print("\n--- CADASTRAR ESTUDANTE ---")

    nome = input("Nome: ")

    idade = int(input("Idade: "))
    while idade <= 0:
        print("A idade deve ser positiva.")
        idade = int(input("Idade: "))

    curso = input("Curso: ")

    notas = []

    for i in range(3):
        nota = float(input(f"Digite a {i + 1}ª nota: "))

        while nota < 0 or nota > 10:
            print("A nota deve estar entre 0 e 10.")
            nota = float(input(f"Digite a {i + 1}ª nota: "))

        notas.append(nota)

    media = calcular_media(notas)
    situacao = calcular_situacao(media)

    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    estudantes.append(estudante)

    print("Estudante cadastrado com sucesso!")


def exibir_estudante(estudante):
    print("\nNome:", estudante["nome"])
    print("Idade:", estudante["idade"])
    print("Curso:", estudante["curso"])
    print("Notas:", estudante["notas"])
    print(f"Média final: {estudante['media']:.2f}")
    print("Situação:", estudante["situacao"])


def listar_estudantes():
    print("\n--- LISTA DE ESTUDANTES ---")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
    else:
        for estudante in estudantes:
            exibir_estudante(estudante)


def consultar_estudante():
    print("\n--- CONSULTAR ESTUDANTE ---")

    nome = input("Digite o nome do estudante: ")

    encontrado = False

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():
            exibir_estudante(estudante)
            encontrado = True
            break

    if not encontrado:
        print("Estudante não encontrado.")


def alterar_dados():
    print("\n--- ALTERAR DADOS ---")

    nome = input("Digite o nome do estudante: ")

    estudante_encontrado = None

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():
            estudante_encontrado = estudante
            break

    if estudante_encontrado is None:
        print("Estudante não encontrado.")
        return

    print("\nEstudante encontrado:")
    exibir_estudante(estudante_encontrado)

    print("\nO que deseja alterar?")
    print("1 - Nome")
    print("2 - Idade")
    print("3 - Curso")
    print("4 - Notas")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        estudante_encontrado["nome"] = input("Novo nome: ")

    elif opcao == 2:
        idade = int(input("Nova idade: "))

        while idade <= 0:
            print("A idade deve ser positiva.")
            idade = int(input("Nova idade: "))

        estudante_encontrado["idade"] = idade

    elif opcao == 3:
        estudante_encontrado["curso"] = input("Novo curso: ")

    elif opcao == 4:
        novas_notas = []

        for i in range(3):
            nota = float(input(f"Digite a {i + 1}ª nota: "))

            while nota < 0 or nota > 10:
                print("A nota deve estar entre 0 e 10.")
                nota = float(input(f"Digite a {i + 1}ª nota: "))

            novas_notas.append(nota)

        estudante_encontrado["notas"] = novas_notas

        nova_media = calcular_media(novas_notas)
        estudante_encontrado["media"] = nova_media
        estudante_encontrado["situacao"] = calcular_situacao(nova_media)

    else:
        print("Opção inválida.")
        return

    print("Dados alterados com sucesso!")


def remover_estudante():
    print("\n--- REMOVER ESTUDANTE ---")

    nome = input("Digite o nome do estudante: ")

    estudante_encontrado = None

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():
            estudante_encontrado = estudante
            break

    if estudante_encontrado is None:
        print("Estudante não encontrado.")
        return

    exibir_estudante(estudante_encontrado)

    confirmacao = input("Deseja realmente remover? (s/n): ")

    if confirmacao.lower() == "s":
        estudantes.remove(estudante_encontrado)
        print("Estudante removido com sucesso!")
    else:
        print("Remoção cancelada.")


def relatorio_turma():
    print("\n--- RELATÓRIO DA TURMA ---")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    total = len(estudantes)

    maior_media = estudantes[0]["media"]
    menor_media = estudantes[0]["media"]

    soma_medias = 0

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for estudante in estudantes:
        media = estudante["media"]

        soma_medias += media

        if media > maior_media:
            maior_media = media

        if media < menor_media:
            menor_media = media

        if estudante["situacao"] == "Aprovado":
            aprovados += 1

        elif estudante["situacao"] == "Recuperação":
            recuperacao += 1

        else:
            reprovados += 1

    media_geral = soma_medias / total

    print("Total de estudantes:", total)
    print(f"Maior média: {maior_media:.2f}")
    print(f"Menor média: {menor_media:.2f}")
    print(f"Média geral: {media_geral:.2f}")
    print("Aprovados:", aprovados)
    print("Recuperação:", recuperacao)
    print("Reprovados:", reprovados)


# Programa principal

while True:
    print("\n========================================")
    print("          SISTEMA ACADÊMICO")
    print("========================================")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Consultar estudante")
    print("4 - Alterar dados")
    print("5 - Remover estudante")
    print("6 - Gerar relatório da turma")
    print("0 - Encerrar sistema")
    print("========================================")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_estudante()

    elif opcao == 2:
        listar_estudantes()

    elif opcao == 3:
        consultar_estudante()

    elif opcao == 4:
        alterar_dados()

    elif opcao == 5:
        remover_estudante()

    elif opcao == 6:
        relatorio_turma()

    elif opcao == 0:
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
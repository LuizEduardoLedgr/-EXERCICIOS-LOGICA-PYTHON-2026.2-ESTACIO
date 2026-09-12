agenda_tel = []
for i in range(5):
  nome = input('digite o nome: ')
  tel = float(input('digite seu numero: '))
  email = input('digite seu e-mail: ')
  agenda_tel.append({
        'nome': nome,
        'telefone': tel,
        'e-mail': email
})
b = input('digite um nome para pesquisa: ')
for contato in agenda_tel:
  if b == contato['nome']:
    print(contato)
    break
  else:
    print('nome não cadastrado')
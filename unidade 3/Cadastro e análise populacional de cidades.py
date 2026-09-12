cidades = []
for i in range(2):
  nome = input('qual o nome da cidade?: ')
  est = input('qual o estado?: ')
  pop = int(input('qual o numero de pessoas?: '))
  cidades.append({
    'nome': nome,
    'estado': est,
    'população': pop
  })
maior = cidades[0]
for cidade in cidades:
  if cidade['população'] > maior['população']:
    maior = cidade
print(maior)
menor = cidades[0]
for cidade in cidades:
  if cidade['população'] < menor['população']:
    menor = cidade
print(menor)
pop_total = 0
for total in cidades:
  pop_total = pop_total + total['população']
print(pop_total)
media = pop_total / 5
print(f"{media:.2f}")
for cidade in cidades:
  print(cidade['nome'])
  print(cidade['estado'])
  print(cidade['população'])
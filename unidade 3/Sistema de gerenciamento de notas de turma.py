turma_a = []
for i in range(3):
  nome = input('qual o nome do aluno?: ')
  nota1 = float(input('digite sua nota: '))
  nota2 = float(input('digite sua nota: '))
  nota3 = float(input('digite sua nota: '))
  media = ((nota1 + nota2 + nota3) / 3)
  turma_a.append({ 
    'nome': nome,
    'notas': [nota1, nota2, nota3],
    'media': media 
})
maior = turma_a[0]
for aluno in turma_a:
  if aluno['media'] > maior['media']:
    maior = aluno
print(maior)
menor = turma_a[0]
for aluno in turma_a:
  if aluno['media'] < menor['media']:
    menor = aluno
print(menor)
apro = 0
recu = 0
repro = 0
for aluno in turma_a:
  if aluno['media'] >= 7:
    apro = apro + 1
  elif 5 <= aluno['media'] < 7:
    recu = recu + 1
  elif aluno['media'] < 5:
    repro = repro + 1
print(turma_a)
print('o numero de aprovados é', apro)
print('o numero de recuperações é', recu)
print('o numero de reprovados é', repro)

temperaturas = []

for i in range(7):
    temperatura = float(input('Qual a temperatura: '))
    temperaturas.append(temperatura)

media = sum(temperaturas) / 7
maior = max(temperaturas)
menor = min(temperaturas)

acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_media += 1

print('\nTemperaturas registradas:', temperaturas)
print('Maior temperatura:', maior)
print('Menor temperatura:', menor)
print('Temperatura média: {:.2f}'.format(media))
print('Dias acima da média:', acima_media)
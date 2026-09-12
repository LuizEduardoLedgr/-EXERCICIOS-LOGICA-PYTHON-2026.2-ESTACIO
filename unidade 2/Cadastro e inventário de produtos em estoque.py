produtos = []

for i in range(5):
    produto = input('Digite o produto: ')
    preço = float(input('Qual o preço do produto: '))
    estoque = int(input('Qual o total do estoque: '))

    produtos.append({
        'nome': produto,
        'preço': preço,
        'estoque': estoque
    })

print("\nProdutos cadastrados:")

for produto in produtos:
    print("\nNome:", produto['nome'])
    print("Preço:", produto['preço'])
    print("Estoque:", produto['estoque'])

total = 0

for produto in produtos:
    total = total + produto['preço'] * produto['estoque']

print("\nValor total do estoque:", total)

maior = produtos[0]

for produto in produtos:
    if produto['preço'] > maior['preço']:
        maior = produto

print("\nProduto com maior preço:")
print("Nome:", maior['nome'])
print("Preço:", maior['preço'])
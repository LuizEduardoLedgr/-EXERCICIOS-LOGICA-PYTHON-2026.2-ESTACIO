frase = input("Digite uma frase: ")

# Remove espaços extras no início e no final
frase = frase.strip()

# Junta múltiplos espaços entre as palavras
palavras = frase.split()

# Quantidade de caracteres, incluindo espaços
print("Quantidade de caracteres:", len(frase))

# Quantidade de palavras
print("Quantidade de palavras:", len(palavras))

# Primeira palavra
print("Primeira palavra:", palavras[0])

# Última palavra
print("Última palavra:", palavras[-1])

# Letra escolhida
letra = input("Digite uma letra: ")

print("Quantidade de ocorrências da letra:",
      frase.lower().count(letra.lower()))

# Maiúsculas
print("Frase em maiúsculas:", frase.upper())

# Minúsculas
print("Frase em minúsculas:", frase.lower())
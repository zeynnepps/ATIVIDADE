
def numero_letras(frase):
    n = len(frase)
    qtd_letra_a = 0

    for i in range (0, n):
        if frase[i] == 'a':
            qtd_letra_a = qtd_letra_a + 1
        return qtd_letra_a
frase = input('Digite sua frase:')

qtd = qtd_letra_a(frase)

print(qtd)


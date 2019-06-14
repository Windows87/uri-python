palavras = raw_input().split(' ')
texto = ""

for palavra in palavras:
    if len(texto):
        if texto[len(texto) - 1] == ".":
            texto += " "

    if palavra[0:2] == palavra[2:4]:
        texto += palavra[2:len(palavra)]
    else:
        texto += palavra
    if palavra[len(palavra) - 1] != ".":
        texto += " "

print texto
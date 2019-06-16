n = input()
palavras = raw_input().split(' ')
texto = ""
i = 0

for palavra in palavras:
    if len(palavra) == 3:
        if palavra[0:2] == 'OB':
            texto += 'OBI'
        elif palavra[0:2] == 'UR':
            texto += 'URI'
        else:
            texto += palavra
    else:
        texto += palavra

    if i != len(palavras) -1:
        texto += " "
    
    i += 1

print texto
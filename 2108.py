big = ""
while True:
    texto = raw_input()
    if texto == '0':
        break

    palavras = texto.split(' ')
    txt = ""
    
    for nIndex in range(len(palavras)):
        txt += str(len(palavras[nIndex]))
        
        if len(big) <= len(palavras[nIndex]):
            big = palavras[nIndex]
        
        if nIndex != len(palavras) - 1:
            txt += "-"
    
    print txt

print ''
print 'The biggest word: ' + big
n = input()

for nIndex in range(n):
    palavras = raw_input().split(' ')
    texto = ""

    for palavra in palavras:
        if palavra != '':
            texto += palavra[0]
    
    print texto
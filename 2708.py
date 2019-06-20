pe = 0
ji = 0

while True:
    texto = raw_input()
    
    if texto == 'ABEND':
        break
    
    saivu, n = texto.split(' ')

    if saivu == 'SALIDA':
        pe += int(n)
        ji += 1
    else:
        pe -= int(n)
        ji -= 1

print pe
print ji

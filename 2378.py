leituras, maximo = raw_input().split(' ')
atual = 0
atingiu = False

for nLeituras in range(int(leituras)):
    saida, entrada = raw_input().split(' ')
    atual += int(entrada) - int(saida)
    if atual > int(maximo):
        atingiu = True
    
if atingiu:
    print "S"
else:
    print "N"
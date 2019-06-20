l = []
l2 = []
maior = 0

while True:
    texto = raw_input()

    if texto == 'FIM':
        break

    nome, simOuNao = texto.split(' ')

    if simOuNao == 'NO':
        l2.insert(len(l2), nome)
        continue

    try:
        l.index(nome)
    except ValueError:
        if maior < len(nome):
            maior = len(nome)
        l.insert(len(l), nome)

ls = sorted(l)
m = ''

for e in l:
    if len(e) == maior:
        m = e
        break

for e in ls:
    print e

ls = sorted(l2)

for e in ls:
    print e

print ""

print "Amigo do Habay:"
print m
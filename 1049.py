x = raw_input()
y = raw_input()
z = raw_input()

if x == 'vertebrado':
    if y == 'ave':
        if z == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if z == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if y == 'inseto':
        if z == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if z == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')

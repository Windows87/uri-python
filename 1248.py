n = input()

for nIndex in range(n):
    alimentos = raw_input()
    alimentosManha = raw_input()
    alimentosAlmoco = raw_input()

    cheat = False
    alimentosRestantes = []

    for alimento in alimentos:
        alimentosRestantes.insert(len(alimentosRestantes), alimento)

    for alimentoManha in alimentosManha:
        try:
            alimentosRestantes.remove(alimentoManha)
        except ValueError:
            cheat = True

    for alimentoAlmoco in alimentosAlmoco:
        try:
            alimentosRestantes.remove(alimentoAlmoco)
        except ValueError:
            cheat = True            

    if cheat:
        print "CHEATER"
        continue

    alimentosRestantes = sorted(alimentosRestantes)
    texto = ""

    for alimentoRestante in alimentosRestantes:
        texto += alimentoRestante

    print texto
x = input()
for i in range(x):
    y = raw_input()
    z = raw_input()

    if y == "ataque" and z == "pedra":
        print "Jogador 1 venceu"
    elif z == "ataque" and y == "pedra":
        print "Jogador 2 venceu"
    elif y == "pedra" and z == "papel":
        print "Jogador 1 venceu"
    elif z == "pedra" and y == "papel":
        print "Jogador 2 venceu"
    elif y == "ataque" and z == "papel":
        print "Jogador 1 venceu"
    elif z == "ataque" and y == "papel":
        print "Jogador 2 venceu"
    elif y == "papel" and z == "papel":
        print "Ambos venceram"
    elif y == "pedra" and z == "pedra":
        print "Sem ganhador"
    elif y == "ataque" and z == "ataque":
        print "Aniquilacao mutua"

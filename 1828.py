x = input()
for i in range(x):
    a, b = (raw_input()).split(' ')
    c = i + 1

    if a == b:
        print "Caso #" + str(c) + ": De novo!"
    elif a == "tesoura" and b == "papel":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "tesoura" and a == "papel":
        print "Caso #" + str(c) + ": Raj trapaceou!"
    elif a == "papel" and b == "pedra":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "papel" and a == "pedra":
        print "Caso #" + str(c) + ": Raj trapaceou!"
    elif a == "pedra" and b == "lagarto":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "pedra" and a == "lagarto":
        print "Caso #" + str(c) + ": Raj trapaceou!"        
    elif a == "lagarto" and b == "Spock":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "lagarto" and a == "Spock":
        print "Caso #" + str(c) + ": Raj trapaceou!"
    elif a == "Spock" and b == "tesoura":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "Spock" and a == "tesoura":
        print "Caso #" + str(c) + ": Raj trapaceou!"
    elif a == "tesoura" and b == "lagarto":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "tesoura" and a == "lagarto":
        print "Caso #" + str(c) + ": Raj trapaceou!"
    elif a == "lagarto" and b == "papel":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "lagarto" and a == "papel":
        print "Caso #" + str(c) + ": Raj trapaceou!"
    elif a == "papel" and b == "Spock":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "papel" and a == "Spock":
        print "Caso #" + str(c) + ": Raj trapaceou!"
    elif a == "Spock" and b == "pedra":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "Spock" and a == "pedra":
        print "Caso #" + str(c) + ": Raj trapaceou!"
    elif a == "pedra" and b == "tesoura":
        print "Caso #" + str(c) + ": Bazinga!"
    elif b == "pedra" and a == "tesoura":
        print "Caso #" + str(c) + ": Raj trapaceou!" 


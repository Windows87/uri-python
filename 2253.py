alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    try:
        pw = raw_input()

        minus = False
        maius = False
        num = False
        invalid = False

        if len(pw) < 6 or len(pw) > 32:
            print "Senha invalida."
            continue
        
        try:
            pw.index(' ')
            print "Senha invalida."
            continue
        except ValueError:
            for caracter in pw:
                try:
                    alfabeto.index(caracter.lower())
                    if caracter.islower():
                        minus = True
                    
                    if caracter.isupper():
                        maius = True

                    if caracter.isdigit() :
                        num = True   
                except ValueError:
                    invalid = True
                    break
            
            if invalid or not minus or not maius or not num:
                print "Senha invalida."
            else:
                print "Senha valida."
    except EOFError:
        break
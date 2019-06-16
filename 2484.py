while True:
    try:
        texto = raw_input()
        i = 0
        for nIndex in range(len(texto)):
            line = ""
            index = 0

            for i2 in range(i):
                line += " "

            for caracter in texto:
                line += caracter

                if(index != len(texto) - 1):
                    line += " "
                
                index += 1
            
            print line
            texto = texto[0:len(texto)-1]
            i += 1
        print ""
    except EOFError:
        break
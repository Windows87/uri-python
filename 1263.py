while True:
    try:
        palavras = raw_input().lower().split(' ')
        ali = 0
        ultima = palavras[0][0]

        for palavrasIndex in range(len(palavras) - 1):
            palavrasIndex += 1
            
            if palavrasIndex != len(palavras) - 1:
                if palavras[palavrasIndex][0] == ultima and palavras[palavrasIndex][0] != palavras[palavrasIndex + 1][0]:
                    ali += 1
            else:
                if palavras[palavrasIndex][0] == ultima:
                    ali += 1

            ultima = palavras[palavrasIndex][0]
        
        print ali
    except EOFError:
        break
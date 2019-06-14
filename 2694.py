n = input()
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for nIndex in range(n):
    texto = raw_input()
    atualN = ""
    sum = 0

    for caractere in texto:
        try:
            nums.index(caractere)
            atualN += caractere
        except ValueError:
            if atualN:
                sum += int(atualN)
            atualN = ""
    
    if atualN:
        sum += int(atualN)

    print sum
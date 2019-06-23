keys = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
    try:
        text = raw_input()
        newText = ''

        for e in text:
            if e == ' ':
                newText += ' '
            else:
                newText += keys[keys.index(e) - 1]
        
        print newText
    except EOFError:
        break
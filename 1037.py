x = float(input())

if x >= 0 and x <= 25:
    print('Intervalo [0,25]')

if x > 25 and x <= 50:
    print('Intervalo (25,50]')

if x > 50 and x <= 75:
    print('Intervalo (50,75]')

if x > 75 and x <= 100:
    print('Intervalo (75,100]')

if x < 0 or x > 100:
    print('Fora de intervalo')

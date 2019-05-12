x = input()

if x >= 0 and x <= 400:
    r = x/100*15
    print("Novo salario: {:.2f}").format(x + r)
    print("Reajuste ganho: {:.2f}").format(r)
    print("Em percentual: 15 %")
elif x >= 400.01 and x <= 800:
    r = x/100*12
    print("Novo salario: {:.2f}").format(x + r)
    print("Reajuste ganho: {:.2f}").format(r)
    print("Em percentual: 12 %")
elif x >= 800.01 and x <= 1200:
    r = x/100*10
    print("Novo salario: {:.2f}").format(x + r)
    print("Reajuste ganho: {:.2f}").format(r)
    print("Em percentual: 10 %")
elif x >= 1200.01 and x <= 2000:
    r = x/100*7
    print("Novo salario: {:.2f}").format(x + r)
    print("Reajuste ganho: {:.2f}").format(r)
    print("Em percentual: 7 %")
else:
    r = x/100*4
    print("Novo salario: {:.2f}").format(x + r)
    print("Reajuste ganho: {:.2f}").format(r)
    print("Em percentual: 4 %")

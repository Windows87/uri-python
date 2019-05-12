a = input()
print(a)
print(str(a/100) + " nota(s) de R$ 100,00")
a = a - a/100 * 100
print(str(a/50) + " nota(s) de R$ 50,00")
a = a - a/50 * 50
print(str(a/20) + " nota(s) de R$ 20,00")
a = a - a/20 * 20
print(str(a/10) + " nota(s) de R$ 10,00")
a = a - a/10 * 10
print(str(a/5) + " nota(s) de R$ 5,00")
a = a - a/5 * 5
print(str(a/2) + " nota(s) de R$ 2,00")
a = a - a/2 * 2
print(str(a) + " nota(s) de R$ 1,00")

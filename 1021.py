a = input()
print("NOTAS:")
print(str(int(a/100)) + " nota(s) de R$ 100.00")
a = a - int(a/100) * 100
print(str(int(a/50)) + " nota(s) de R$ 50.00")
a = a - int(a/50) * 50
print(str(int(a/20)) + " nota(s) de R$ 20.00")
a = a - int(a/20) * 20
print(str(int(a/10)) + " nota(s) de R$ 10.00")
a = a - int(a/10) * 10
print(str(int(a/5)) + " nota(s) de R$ 5.00")
a = a - int(a/5) * 5
print(str(int(a/2)) + " nota(s) de R$ 2.00")
a = a - int(a/2) * 2
print("MOEDAS:")
print(str(int(a)) + " moeda(s) de R$ 1.00")
a = a - int(a)
print(str(int(a/0.5)) + " moeda(s) de R$ 0.50")
a = round(a - int(a/0.5) * 0.5, 2)
print(str(int(a/0.25)) + " moeda(s) de R$ 0.25")
a = round(a - int(a/0.25) * 0.25, 2)
print(str(int(a/0.1)) + " moeda(s) de R$ 0.10")
a = round(a - int(a/0.1) * 0.1, 2)
print(str(int(a/0.05)) + " moeda(s) de R$ 0.05")
a = round(a - int(a/0.05) * 0.05, 2)
print(str(int(a/0.01)) + " moeda(s) de R$ 0.01")

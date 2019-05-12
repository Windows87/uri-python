a = input()
print(str(a/365) + " ano(s)")
a = a - a/365 * 365
print(str(a/30) + " mes(es)")
a = a - a/30 * 30
print(str(a) + " dia(s)")

a, b, c, d = (raw_input()).split(' ')
a = float(a)
b = float(b)
c = float(c)
d = float(d)

m1 = (a*2 + b*3 + c*4 + d)/10
print("Media: {:.1f}").format(m1)

if m1 >= 7:
    print("Aluno aprovado.")
elif m1 < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    e = input()
    print("Nota do exame: {:.1f}").format(e)
    m1 = (m1 + e)/2

    if m1 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: {:.1f}").format(m1)

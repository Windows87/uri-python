nam = []
nam2 = []
nam3 = []

while True:
    try:
        n = raw_input()
        nam.insert(len(nam), n)
        nam2.insert(len(nam2), n.lower())
        nam3.insert(len(nam3), n.lower())
    except EOFError:
        break

nam2 = sorted(nam2, reverse=True)[0]
print nam[nam3.index(nam2)]
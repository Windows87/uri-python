while True:
    try:
        n = input()
        ids = []

        for nIndex in range(n):
            ids.insert(nIndex, raw_input())
        
        ids = sorted(ids)

        for id in ids:
            print id
    except EOFError:
        break
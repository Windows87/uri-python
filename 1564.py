while True:
    try:
        x = input()
        if x > 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
    except EOFError:
        break

    

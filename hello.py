re = True
while re == True :
    a = int(input("donne un nombre"))
    b=1
    for i in range(10):
        c = a * b
        b=b+1
        print(c)
    d = input("pour recommencer le programme taper sur 'r' ou taper sur une autre touches pour términer le programme")
    if d == "r":
        re = True
    else :
        re = False

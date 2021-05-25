def changeChr(string=input('enter your str')):
    l1=list(string)
    l=len(l1)
    for a in range(0,l):
        b=l1[a]
        c=ord(l1[a])
        if c>=97:
            c=c-32
            print(chr(c),end='')
        else:
            c=c+32
            print(chr(c),end='')
changeChr()

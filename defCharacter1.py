def changechr(str=input('enter your str')):
    s=""
    for i in range(0,len(str)):
        if str[i].islower()==True:
            s+=str[i].upper()
        else:
            s+=str[i].lower()
    print(s)
changechr()

def get_name(name=input('enter your name'),encode=True):
    if encode==True:
        def FindCodeAndChange(name):
            l1=list(name)
            l=len(l1)
            for a in range(0,l):
                b=l1[a]
                c=ord(b)
                if c>=97:
                    c=c-32
                else:
                    c=c+32
                print(c,end=' ')
        FindCodeAndChange(name)
    else:
        l1=name
        l2=l1.split()
        l=len(l2)
        for a in range(0,l):
            b=int(l2[a])
            if b>=97:
                b=b-32
            else:
                b=b+32
            c=chr(b)
            print(c,end='')
get_name(encode=False)
    
    

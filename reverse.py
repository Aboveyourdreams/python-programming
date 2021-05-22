def ReverseList():
    A=str(input("enter your str"))
    a=1
    x=len(A)
    start=A[0]
    while 0<=x-a:
        end=A[x-a]
        print(end,end="")
        a=a+1
ReverseList()

a=int(input('enter your number'))
b=0
if a>1:
    for c in range(1,a+1):
        if a % c == 0:
            b+=1
if b == 2:
    print('your number is prime')  
else:
    print('your number is not prime')
 

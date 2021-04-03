x=int(input('enter your first number'))
a=set()
s1=['-','+','*','/']
signs=set(s1)
y=input('enter your mathematical sign')
while y not in s1:
    input('enter your mathematical sign')
z=int(input('enter your second number'))
if y=='+':
    print(x,y,z,'=',x+z)
elif y=='-':
    print(x,y,z,'=',x-z)
elif y=='*':
    print(x,y,z,'=',x*z)
elif y=='/':
    print(x,y,z,'=',x/z)

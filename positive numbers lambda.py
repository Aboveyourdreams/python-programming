a=0
b=0
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
while a<15:
    x=int(input('enter your number'))
    numbers[b]=x #to replace value in the list 'numbers'
    a+=1
    b+=1
positiveNumbers=list(filter(lambda x: x>0, numbers))
print(positiveNumbers)

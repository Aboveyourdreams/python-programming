#To make a Exception class for call later.
class NotValidError(Exception):
    pass


#Main class that contains methodes.
class Main:
    def __init__(self):
        self.opening='''
Hello, you can choose a program from list below:
1-Factorial
2-Fibonacci
3-Min and Max
4-Prime Number
5-Calculator
6-Def Character
7-Encode Decode
8-Count String
9-Vowel Sound
10-Decorator
Enter "END" to exit.
'''


#Returns the table of content.
    def start(self):
        return self.opening



    
#Calculates the factorial of entered number.
    def fact1(self):
        try:
            a=int(input("Enter your number:"))
            def factorial(a):
                for x in range(1,a):
                    b=a*x
                print('Factorial of',a,'is',b)   
            if a!=5:
                factorial(a)
                
            else:
                factorial(6)
                raise ValueError("I cant calculate factorial of 5 :|")
        except ValueError as ve:
            print(ve)
                


        

#Calculates the fibonacci to entered number.
    def fibo2(self):
        try:
            n=int(input("Enter your number:"))
            a=1
            b=0
            while a<=n:
                print(b)
                c=a+b
                b=a
                a=c
            print(b)
        except ValueError as ve:
            print(ve)
      
            
        
#Shows greatest and least numbers.
    def minmax3(self):
        try:
            x=input('Enter your numbers')
            a=x.split(' ')
            for n in a:
                n=float(n)
            min_num=a[0]
            max_num=a[0]
            for FirstNumber in a:
                if float(max_num)<float(FirstNumber):
                    max_num=FirstNumber
                elif float(min_num)>float(FirstNumber):
                    min_num=FirstNumber
            print('Graetest number is:',max_num,'and Least number is:',min_num)
            try:
                for n in a:
                    if 10<=float(n)<=100:
                        raise NotValidError('Numbers between 10 and 100 are unaccepted')
            except NotValidError as nve:
                for n in a:
                    if 10<=float(n)<=100:
                        print(nve)
        except ValueError as ve:
                print(ve)




#Shows that antered number is prime or it is not.
    def prime4(self):
        try:
            a=int(input('Enter your number:'))
            b=0
            if a>1:
                for c in range(1,a+1):
                    if a % c == 0:
                        b+=1
            if b == 2:
                print('Your number is prime.')  
            else:
                print('Your number is not prime.')
        except ValueError as ve:
            print(ve)
            



#Takes two numbers and a sign to calculate.
    def calculator5(self):
        try:
            x=int(input('Enter your first number:'))
            L1=['-','+','*','/']
            y=str(input('Enter your mathematical sign:'))
            while y not in L1:
                input('Enter your mathematical sign:')
            z=int(input('Enter your second number:'))
            if y=='+':
                print(x,y,z,'=',x+z)
            elif y=='-':
                print(x,y,z,'=',x-z)
            elif y=='*':
                print(x,y,z,'=',x*z)
            elif y=='/':
                print(x,y,z,'=',x/z)
        except ValueError as ve:
            print(ve)




            
#Changes uppercase to lowercase and lowercase to uppercase.
    def character6(self):
        def changeChr(string=input('Enter your sentence:')):
            l1=list(string)
            l=len(l1)
            for a in range(0,l):
                b=l1[a]
                c=ord(l1[a])
                if 65<=c<=90 or 97<=c<=122:
                    if c>=97:
                        c=c-32
                        print(chr(c),end='')
                    else:
                        c=c+32
                        print(chr(c),end='')
                else:
                    print('You must enter some characters.')
                    break
        changeChr()
            




#To Encode and Decode.
    def encodedecode7(self):
       def get_name(name=input('Enter your name:'),encodeType=input('To encode enter "Encode" and "Decode" to decode:')):
            if encodeType.lower()=='encode':
                def FindCodeAndChange(name,encodeType):
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
                FindCodeAndChange(name,encodeType)
            elif encodeType.lower()=='decode':
                try:
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

                except:
                        print('Not Found')
            else:
                raise ValueError()

            get_name()
       


#To count 'Freezeman' in entered sentence.
    def count8(self):
        a=input('Enter your string:')
        counter1=0
        sentence=''
        counter2=0
        if len(a)<10:
            a='python language tutorials by freezeman'
            print('Defualt sentence has been choosen.')
        x=a.split()

        for i in x:
            if 'freezeman' in i.lower():
                counter2=counter2+1
        for j in a:
            sentence=sentence+j
            counter1=counter1+1
            if 'freezeman' in sentence.lower():
                counter1=counter1-9
                break
            if j=='':
                sentence=''
                continue
        print('Repeated time of freezeman is',counter2,'and the first index is',counter1,'.')
                                                      
                    
            
            


#To find vowel sounds in entered string.
    def vowel9(self):
        x=input('Enter your string:')
        a=0
        e=0
        i=0
        o=0
        u=0
        for first in x:
            if first=='a' or first=='A':
                a=a+1
            elif first=='e' or first=='E':
                e=e+1
            elif first=='i' or first=='I':
                i=i+1
            elif first=='o' or first=='O':
                o=o+1
            elif first=='u' or first=='U':
                u=u+1
        print('a=',a,', ','e=',e,', ','i=',i,', ','o=',o,', ','u=',u)




#To do division between entered numbers.
    def decorator10(self):
        try:
            def getFunction(function):
                def checkValue(num1,num2):
                    if num1!=0 and num2!=0:
                        return function(num1,num2)
                    else:
                        raise ValueError('Number that you entered is zero.')
                return checkValue

            number1=int(input('Enter your first number:'))
            number2=int(input('Enter your second number:'))

            @getFunction
            def div(number1,number2):
                return number1/number2
            res =div(number1,number2)
            print(res)

        except ValueError as ve:
            print(ve)
            
            
m=Main()

while True:
    try:

        print(m.start())
        commander = input('Enter number of program or "End" to exit:')
            
        if commander.upper()=='END':
            exit(0)

        commander = int(commander)

        if commander > 10 or commander < 0:
            raise ValueError('Out of range.')

        if commander == 1:
            m.fact1()
        
        elif commander == 2:
            m.fibo2()

        elif commander == 3:
            m.minmax3()

        elif commander == 4:
            m.prime4()

        elif commander == 5:
            m.calculator5()

        elif commander == 6:
            m.character6()

        elif commander == 7:
            m.encodedecode7()

        elif commander == 8:
            m.count8()

        elif commander == 9:
            m.vowel9()

        elif commander == 10:
            m.decorator10()
 
    except ValueError as ve:
        print(ve)
        continue

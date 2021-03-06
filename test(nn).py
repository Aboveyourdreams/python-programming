from random import *

# To make a Exception class for call later.
class NotValidError(Exception):
    pass


# Main class that contains methodes.
class Main:
    def __init__(self):
        self.opening = '''
Hello, you can choose a program from list below:
1-Factorial
2-Fibonacci
3-Min and Max
4-Prime Number
5-Calculator
6-Lower-Upper
7-Encode Decode
8-Count String
9-Vowel Sound
10-Decorator
Enter "END" to exit.
'''

    # Returns the table of content.
    def start(self):
        return self.opening

    # Calculates the factorial of entered number.
    def fact1(self):
        while True:
            try:
                a = input("Enter your number: ")
                if a.upper() == "END":
                    exit(0)
                else:
                    a = int(a)

                def factorial(a):
                    fact = 0
                    res = 1
                    if a < 1:
                        print('Input value is incorrect')
                    for number in range(1, a + 1):
                        res = res * number
                    print('Factorial of', a, 'is', res)

                if a != 5:
                    factorial(a)

                else:
                    raise ValueError
                
            except ValueError as ve:
                if a == "5" or a == 5:
                    print("I cant calculate factorial of 5 :|")
                    factorial(6)
                    break
                else:
                    print(ve)
                    continue
            else:
                break

    # Calculates the fibonacci to entered number.
    def fibo2(self):
        while True:
            try:
                n = input("Enter your number: ")
                if n.upper() == "END":
                    exit(0)
                else:
                    n = int(n)
                a = 1
                b = 0
                while a <= n:
                    print(b)
                    c = a + b
                    b = a
                    a = c
                print(b)
            except ValueError as ve:
                print(ve)
                continue
            else:
                break

    # Shows greatest and least numbers.
    def minmax3(self):
        while True:
            try:
                print('You should separate the numbers with just one single space')
                x = input('Enter your numbers: ')
                if x.upper() == "END":
                    exit(0)
                a = x.split(' ')
                for n in a:
                    n = float(n)
                min_num = a[0]
                max_num = a[0]
                for FirstNumber in a:
                    if float(max_num) < float(FirstNumber):
                        max_num = FirstNumber
                    elif float(min_num) > float(FirstNumber):
                        min_num = FirstNumber
                print('Graetest number is:', max_num, 'and Least number is:', min_num)
                try:
                    for n in a:
                        if 10 <= float(n) <= 100:
                            raise NotValidError('Numbers between 10 and 100 are unaccepted')
                except NotValidError as nve:
                    for n in a:
                        if 10 <= float(n) <= 100:
                            print(nve)
            except ValueError as ve:
                print(ve)
                continue
            else:
                break

    # Shows that antered number is prime or it is not.
    def prime4(self):
        while True:
            try:
                a = input('Enter your number: ')
                if a.upper() == "END":
                    exit(0)
                else:
                    a = int(a)
                b = 0
                if a > 1:
                    for c in range(1, a + 1):
                        if a % c == 0:
                            b += 1
                if b == 2:
                    print('Your number is prime.')
                else:
                    print('Your number is not prime.')
                    continue
            except ValueError as ve:
                print(ve)
                continue
            else:
                break

    # Takes two numbers and a sign to calculate.
    def calculator5(self):
        while True:
            try:
                x = input('Enter your first number: ')
                if x.upper() == "END":
                    exit(0)
                else:
                    x = int(x)
                L1 = ['-', '+', '*', '/']
                y = str(input('Enter your mathematical sign: '))
                if y.upper() == "END":
                    exit(0)
                while y not in L1:
                    y = input('Enter your mathematical sign: ')
                    if y in L1:
                        break
                    elif y.upper() == "END":
                        exit(0)
                z = input('Enter your second number: ')
                if z.upper() == "END":
                    exit(0)
                else:
                    z = int(z)
                if y == '+':
                    print(x, y, z, '=', x + z)
                elif y == '-':
                    print(x, y, z, '=', x - z)
                elif y == '*':
                    print(x, y, z, '=', x * z)
                elif y == '/':
                    print(x, y, z, '=', x / z)
            except ValueError as ve:
                print(ve)
                continue
            else:
                break

    # Changes uppercase to lowercase and lowercase to uppercase.
    def character6(self):
        while True:
            try:
                # flag = False
                def changeChr(string):
                    # nonlocal flag
                    l1 = list(string)
                    l = len(l1)
                    for a in range(0, l):
                        b = l1[a]
                        c = ord(l1[a])
                        if 65 <= c <= 90 or 97 <= c <= 122:
                            if c >= 97:
                                c = c - 32
                                print(chr(c), end='')
                                # flag = False
                            elif c <= 90:
                                c = c + 32
                                print(chr(c), end='')
                                # flag = False
                            
                        else:
                            # print('You must enter some characters.', end='')
                            print(b,end='')
                            # flag = True
                            continue

                string = input('\nEnter your sentence: ')
                if string=='':
                   print("you enter empty value! :|")
                   continue

                if string.upper() == "END":
                    exit(0)
                else:
                    changeChr(string)
                # if flag == True:
                #     flag = False
                #     continue

            except ValueError as ve:
                print(ve)
                continue
            else:
                break

    # To Encode and Decode.
    def encodedecode7(self):
        while True:
            try:

                    letters = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]
                    originallet = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]

                    def encrypt():
                        text = input("Enter your text: ")
                        if text.upper() == "END":
                            exit(0)
                        rand_n = randint(10,99)

                        for i in range(rand_n) :
                            fakenum = letters[0]
                            letters.remove(fakenum)
                            letters.append(fakenum)

                        finaltext = ""
                        for i in text :
                            number = originallet.index(i)
                            finaltext += letters[number]

                        chars = ["!","@","#","$","%","^","&","*","(","0","<",">","?","/","|","~"]

                        f_text_list = []
                        for i in finaltext :
                            f_text_list.append(i)

                        for i in range(len(f_text_list)):
                            char = chars[randint(0,len(chars)-1)]
                            f_text_list.insert(i*2,char)

                        f2_list = f_text_list[::-1]

                        rand_s = str(rand_n)

                        f2_list.insert(0,rand_s[0])
                        f2_list.append(rand_s[1])


                        f_text = ""

                        for i in f2_list :
                            f_text += i

                        print(f_text)

                    def decrypt():    


                        ramzide = input("Enter you encrypted text: ")
                        if ramzide.upper() == "END":
                            exit(0)
                        num = ""
                        num += ramzide[0]
                        num += ramzide[len(ramzide)-1]
                        ramz_list = []
                        for i in ramzide :
                            ramz_list.append(i)
                        ramz_list.pop(0)
                        ramz_list.pop(len(ramz_list)-1)

                        chars = ["!","@","#","$","%","^","&","*","(","0","<",">","?","/","|","~"]
                        for i in range(10):
                            for i in chars:
                                if i in ramz_list:
                                    ramz_list.remove(i)



                        ramz_list = ramz_list[::-1]


                        for i in range(int(num)) :
                            fakenum = letters[0]
                            letters.remove(fakenum)
                            letters.append(fakenum)

                        finaltext = ""
                        for i in ramz_list :
                            number = letters.index(i)
                            finaltext += originallet[number]

                        print(finaltext)

                    ok = "y"
                    while ok == "y" :  
                        choice = input("Encode or Decode?(e/d) " )
                        if choice.upper() == "END":
                            exit(0)
                        elif choice.lower() == "e" :
                            encrypt()
                        elif choice.lower() == 'd' :
                            decrypt()
                        else :
                            raise ValueError("It is a wrong input")

                        ok = input("Do you want to continue?? (y/n)")
                        letters = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'," "]

            except ValueError as ve:
                print(ve)
                continue
            else:
                break

    # To count 'Freezeman' in entered sentence.
    def count8(self):
        a = input('Enter your string:')
        if a.upper() == "END":
            exit(0)
        counter1 = 0
        sentence = ''
        counter2 = 0
        if len(a) < 10:
            a = 'python language tutorials by freezeman'
            print('Defualt sentence has been choosen.')
        x = a.split()

        for i in x:
            if 'freezeman' in i.lower():
                counter2 = counter2 + 1
        for j in a:
            sentence = sentence + j
            counter1 = counter1 + 1
            if counter2>0:
                if 'freezeman' in sentence.lower():
                    counter1 = counter1 - 9
                    break
                if j == '':
                    sentence = ''
                    continue
            else:
                counter1=0
        print('Repeated time of freezeman is', counter2, 'and the first index is', counter1, '.')

    # To find vowel sounds in entered string.
    def vowel9(self):
        x = input('Enter your string:')
        if x.upper() == "END":
            exit(0)
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0
        for first in x:
            if first == 'a' or first == 'A':
                a = a + 1
            elif first == 'e' or first == 'E':
                e = e + 1
            elif first == 'i' or first == 'I':
                i = i + 1
            elif first == 'o' or first == 'O':
                o = o + 1
            elif first == 'u' or first == 'U':
                u = u + 1
        print('a=', a, ', ', 'e=', e, ', ', 'i=', i, ', ', 'o=', o, ', ', 'u=', u)

    # To do division between entered numbers.
    def decorator10(self):
        while True:
            try:
                def getFunction(function):
                    def checkValue(num1, num2):
                        if num1 != 0 and num2 != 0:
                            return function(num1, num2)
                        else:
                            raise ValueError('Number that you entered is zero.')

                    return checkValue

                number1 = input('Enter your first number:')
                if number1.upper() == "END":
                    exit(0)
                else:
                    number1 = int(number1)
                number2 = input('Enter your second number:')
                if number2.upper() == "END":
                    exit(0)
                else:
                    number2 = int(number2)

                @getFunction
                def div(number1, number2):
                    return number1 / number2

                res = div(number1, number2)
                print(res)

            except ValueError as ve:
                print(ve)
                continue
            else:
                break


m = Main()

while True:
    try:

        print(m.start())
        commander = input('Enter number of program or "End" to exit:')

        if commander.upper() == 'END':
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

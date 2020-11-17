import math
import random




def zad1():
    a = int(input("Wybierz pierwsza liczbe "))
    b = int(input('Wybierz drugą liczbę '))
    def nwd(a, b):
        i = 1
        c = 1
        while (a >= i) and (b >= i):
            if (a % i == 0) and (b % i == 0):
                c = i
            i = i + 1
        print(c)
    nwd(a, b)

def zad2():
    a = int(input('Jaka jest temperatura '))
    def checking_temp(x):
        if x <= 5:
            print("Pizga fest")
        elif 5 < x <= 20:
            print('Jest średnio ciepło')
        else:
            print('cieplotuko')
    checking_temp(a)
def zad3():
    i = 9
    while i<= 21:
        print(i)
        i = i + 3
def zad4():
    i = 1.8
    while i >= 0.8:
        print(round((i),2))
        i = i - 0.1
def zad5():
    i = 1
    while True:
        i = i + 1
        print(i)
def zad9():
    h = 'asffflk 42142 3dsa'
    a = ''
    for i in h:
        if i == ' ':
            a = a + ' '
        else:
            a = a + str('*')
    print(a)


def fib(n):
    i = 1
    a, b = 0, 1
    while i < 10:
        print(a)
        print(b)
        i += 1
        a = a + b
        b = b + a
def test():
    a = 0
    try:
        print(str(a) + "th swipe")
        a += 1
        print(str(a) + "th swipe left")
    except:
        pass
#FUNKCJE
def zad1(a):
    x = (a * 1.8) + 32
    print('Temperatura w Fahrenheitach')
    return x

#



i = 10
def f():
    print(i)
f() #10
i=42
f() #42

def addf(x,y):
    print(x+y)
i1 = 23
i2 = 12
addf(i1,i2)#35

def myreturn(x,y):
    return x*y
i3 = 2
i5 = 5
i8 = myreturn(i3,i5)
print(i8)#10

def myreturn2(a, x=2, y=3):
    return a*x*y
i3 = 2
i5 = 5
i8 = myreturn2(8,i3,i5)
print(i8)#80
i8 = myreturn2(8)
print(i8)#48

def factorial(n):#遞回函數
    if (n==0):
        return 0 
    if (n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(1))#1
print(factorial(2))#2
print(factorial(3))#6
print(factorial(4))#24
print(factorial(5))#120

def  fibonaci(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
print(fibonaci(1))#1
print(fibonaci(2))#1
print(fibonaci(3))#2
print(fibonaci(4))#3
print(fibonaci(5))#5



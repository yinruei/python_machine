class Myclass:
    i=12345
print(Myclass.i)

class Complex:
    def __init__(self,realpart,imagepart):
        self.r = realpart
        self.i = imagepart
x = Complex(3.0,-4.5)
print(x.r,x.i)
# x2 = Complex()#會出錯，需要兩個參數

class Dog:
    kind = 'small dog'
    def __init__(self,name):
        self.name = name
d=Dog('SmallDog')
e=Dog('very small dog')
print(type(d))#<class '__main__.Dog'>屬於Dog 類別的物件
print(type(e))#<class '__main__.Dog'>屬於Dog 類別的物件
print(d.name)
print(e.name)

class Complex2:
    def __init__(self,realpart,imagepart):
        self.r = realpart
        self.i = imagepart
    def __del__(self):
        print("物件被解構刪除了")
x = Complex2(3.0,-4.5)
print(x.r,x.i)
x=None
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age  = age
        self.color= color

Cats = [Cat('Kitty', 1, 'white')
        ,Cat('Annie', 3, 'gold')
        ,Cat('Elsa', 5, 'gold')
        ,Cat('Kiki', 7, 'black')
        ,Cat('Lily', 4, 'white')]

# 找出最大的年紀數字
print("Cat largest age is {}".format(max([i.age for i in Cats])))
# print("Cat name are:  {}".format([i.name for i in Cats]))
# print("Cat color has:  {}".format([i.color for i in Cats]))

# 可以有另一種寫法?
'''
上面用1行就解決，下面用了4行才解決
'''
data=[]
for i in Cats:  
    data.append(i.age)
print("Cat largest age is {}".format(max(data)))

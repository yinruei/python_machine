class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
    
jonny = NamedList('John Paul Jones')
print(type(jonny))
print(dir(jonny))

jonny.append("Bass Player")
jonny.extend(["Composer", "Arranger", "Musician"])
print(jonny)
print(jonny.name)

print('-----------------------')
for attr in jonny:
    print(jonny.name + " is a " + attr + ".")
class Vehicle:
    def __init__(self,name,engine):
        self.__name=name
        self.__engine=engine

    def getName(self):
        return self.__name
    def getEngine(self):
        return self.__engine

class Car(Vehicle):
    def __init__(self,name,engine,electric):
        super().__init__(name,engine)##super呼叫父類別的建構函數
        self.__electric = electric

    def getEngine(self):
        return ("超級")
    
    def getAuto(self):
        print("自動駕駛車")

myCar=Car("特斯拉","磁電engine","電力")
myCar.getAuto()
print(myCar.getEngine())
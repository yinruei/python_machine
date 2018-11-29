class Vehicle:
    def __init__(self,name,engine):
        self.__name=name
        self.__engine=engine

    def getName(self):
        return self.__name
    def getEngine(self):
        return self.__engine
    def setEngine(self,engine):
        self.__engine = engine
    
class Car(Vehicle):
    def __init__(self,name,engine,electric):
        super().__init__(name,engine)##super呼叫父類別的建構函數
        self.__electric = electric

    def getCarName(self):
        print("名字"+self.getName())
        print("引勤"+self.getEngine())
        print("電動車"+self.__electric)

    def getAuto(self):
        print("自動駕駛車")
    
myCar = Car("特斯拉","磁電engine","電力")
# myCar.getCarName()
print(myCar.getAuto())
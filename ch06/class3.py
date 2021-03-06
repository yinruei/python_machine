class Vehicle:
    def __init__(self,name,engine):
        self.__name=name##__私有存取，private的存取權限，只有在該類別方法才能存取
        self.__engine=engine

    def getName(self):
        return self.__name
    def getEngine(self):
        return self.__engine
    def setEngine(self,engine):
        self.__engine=engine

class Electric:
    def __init__(self,PowerElectric):
        self.__PowerElectric=PowerElectric

    def getPower(self):
        return self.__PowerElectric

    def setPower(self,PowerElectric):
        self.__PowerElectric=PowerElectric

class Car(Vehicle,Electric):
    def __init__(self,name,engine,PowerElectric,auto):
        super().__init__(name,engine)
        self.setPower(PowerElectric)#####只是將setPower設定給Car裡面的Electric的屬性，把他設進來
        self.__Auto=auto

    def getCarName(self):
        print("名字"+self.getName())
        print("引擎"+self.getEngine())
        print("電動車"+self.getPower())
    
    def getAuto(self):
        return self.__Auto

myCar = Car("特斯拉","磁電引擎","電力","自動駕駛車")
# print(myCar)
myCar.getCarName()
# myCar.getAuto()

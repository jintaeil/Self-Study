# 복습하기
# abc = abstract base class의 약자이다.
from abc import abstractmethod, ABCMeta
class Mobile (metaclass=ABCMeta):
    __mobileName = 'NONAME'      # 캡슐화 작업
    __batterySize = 0
    __osType = 0

    def __int__(self,mobileName,batterySize,osType): # 생성자
        self.__mobileName = mobileName
        self.__batterySize = batterySize
        self.__osType = osType

    # @property # --> get 또는 property를 사용하여 get메소드를 표현 : 값을 불러오는데 사용
    def getmobileName(self):
        return self.__mobileName
    # @mobileName.setter
    def setmobileName(self,mobileName):
        self.__mobileName = mobileName
    def getbatterySize(self):
        return self.__batterySize
    def setbatterySize(self,batterySize):
        self.__batterySize = batterySize
    def getosType(self):
        return self.__osType
    def setosType(self,osType):
        self.__osType = osType

    @abstractmethod
    def operate (self,time):
        pass

class IChange(metaclass=ABCMeta):
    @abstractmethod
    def charge (self,time):
        pass

class Ltab(Mobile,IChange) :

    def operate(self,time):
        BS = super().getbatterySize() #BS = batterySize
        x = time * 10
        super().setbatterySize(BS-x)
        return super().getbatterySize()
    def charge(self,time):
        BS = super().getbatterySize()
        x = time * 10
        super().setbatterySize(BS+x)
        return super().getbatterySize()

class Otab(Mobile,IChange) :

    def operate(self,time):
        BS = super().getbatterySize() #BS = batterySize
        x = time * 12
        super().setbatterySize(BS-x)
        return super().getbatterySize()
    def charge(self,time):
        BS = super().getbatterySize()
        x = time * 8
        super().setbatterySize(BS+x)
        return super().getbatterySize()


# 출력을 못하여 실패....
# 추가로 공부해야겠다...
'''
if __name__ == '__main__':
    a1 = Ltab('Ltab','100','AP-01')
    a2 = ('Otab', 1000, 'AND-20')

    print("Mobile\t\tBattery\t\tOS")
    print("---------------------------")
    print(f'{a1.mobileName}\t\t{a1.batterySize}\t\t{a1.osType}')
    print(a2.getmobileName()\t\t{a2.getbatterySize()}\t\t{a2.getosType()}')
    print("---------------------------")
    print()
    a1.charge("10분 충전")
    a2.charge("10분 충전")
    print("Mobile\t\tBattery\t\tOS")
    print("---------------------------")
    print(f'{a1.mobileName}\t\t{a1.batterySize}\t\t{a1.osType}')
    print(f'{a2.mobileName}\t\t{a2.batterySize}\t\t{a2.osType}')
    print("---------------------------")
    print()
    print("5분 통화")
    a1.operate(5)
    a2.operate(5)
    print("Mobile\t\tBattery\t\tOS")
    print("---------------------------")
    print(f'{a1.mobileName}\t\t{a1.batterySize}\t\t{a1.osType}')
    print(f'{a2.mobileName}\t\t{a2.batterySize}\t\t{a2.osType}')
    print("---------------------------")
'''
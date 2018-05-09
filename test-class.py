class YilanteCar(object):

    def move(self):
        print("---Yilante车在移动————")

    def stop(self):
        print("----Yilante停车-----")


class SonataCar(object):

    def move(self):
        print("---Sonata车在移动————")

    def stop(self):
        print("----Sonata停车-----")

class CarStore(object):

    def __init__(self):
        self.carFactory = CarFactory()

    def order(self, typeName):

        self.car = self.carFactory.createCar(typeName)
        self.car.move()
        self.car.stop()

class CarFactory(object):

    def createCar(self, typeName):
        self.typeName = typeName
        if self.typeName == "1111":
           self.car = YilanteCar()
        elif self.typeName == "2222":
             self.car = SonataCar()
        return self.car

a = CarStore()

a.order("2222")

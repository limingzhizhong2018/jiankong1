class CakeStore(object):
    def __init__(self):
        self.factory = CakeFactory()
    def taste(self, weidao):
        cake = self.factory.createCake(weidao)
        print("cake的味道：%s----"%cake.taste)

class CakeFactory(object):
    def createCake(self, weidao):
        if weidao == "1":
            cake = OrangeCake()
        elif weidao == "2":
            cake = AppleCake()
        return cake

class OrangeCake(object):
    def __init__(self, weidao = "1"):
        self.taste = weidao

class AppleCake(object):
    def __init__(self, weidao = "2"):
        self.taste =weidao

a = CakeStore()
a.taste("2")
class Player:
    def __init__(self,health,name):
        self.health = health
        self.name = name
    def __str__(self):
        return str(self.name) + "的生命值" + str(self.health)
    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)
class Danjia:
    def __init__(self,rongliang):
        self.rongliang = rongliang
        self.rongnalist = []
    def __str__(self):
        return "弹夹当前数量："+str(len(self.rongnalist)) + "/" + str(self.rongliang)
    def baocunzidan(self,zidan):
        if len(self.rongnalist) < self.rongliang:
            self.rongnalist.append(zidan)



class Zidan:
    pass
class Qiang:
    pass

laowang = Player("100","laowang")
print(laowang)

danjia = Danjia(20)
print(danjia)




zidan=Zidan()





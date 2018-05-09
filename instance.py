class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True


a = Singleton(11, "hahah")
b = Singleton(22, "heheh")

print(a)
print(id(a))
print(a.name)
print(a.age)
print(b)
print(id(b))
print(b.name)
print(b.age)

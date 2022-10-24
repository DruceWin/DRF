from abc import ABC, abstractmethod

class MyABC(ABC):
    @abstractmethod
    def sayHi(self):
        return print(1)

    @abstractmethod
    def sayBy(self):
        pass


class User(MyABC):
    def sayHi(self):
        print(2+2)

    def sayBy(self):
        print("Hi")


u1 = User()
print(u1)
u1.sayHi()
u1.sayBy()
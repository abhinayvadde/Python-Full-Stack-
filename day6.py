'''
# Inheritance Concept
class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello")

class child(Parent):

    def sound(self):
        print(f"I'm {self.name} and my age is {self.age}")


c1 = child("Abhi",21)
c1.sound()

'''
# Single Level (From parent to the child)
class parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello")

class child(parent):
    def sound(self):
        print(f"I'm {self.name} and my age is {self.age}")

c1 = child("Abhi", 21)
c1.greet()
c1.sound()


# Hierarchical Inheritance (From parent to child and child to child)

class Child2(parent):
    def sound2(self):
        print("hierarchical inheritence")

    def car(self):
        print("I,m having lambo")

c2 = Child2("Rohit", 22)
c2.car()
c2.sound2()


# Multiple Inheritance (From parent to child and child to child and child to child) and Multi-level
class GrandChild(child,Child2):
    def sound(self):
        print(f"I'm {self.name} , implementing multi level inheritence")

g1 = GrandChild("Rohit", 22)
g1.sound()





# Encapsulation Concept

class Bank:
    def __init__(self,acc,balance):
        self.__acc = acc
        self.__balance = balance
        print("Bank Account Created")

    def get_balance(self):
        print(self.__balance)

    def set_balance(self,amount):
        self.__balance += amount

Kotak = Bank("saving",1000)
Kotak.set_balance(2000)
Kotak.get_balance()






#Method over loading

def add(a=0,b=0,c=0):
    print(a+b+c)


add(1,2)


#Abstration

from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def b(self):
        pass

class BMW(Car):

    def b(self):
        print("breaks applied")

car1 = BMW()
car1.b()
      



class Phone:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def mobile(self):
        print(f"This is {self.brand} {self.model}")


class Vivo(Phone):

    def call(self):
        print(f"Calling from {self.brand} ...")

class Iqoo(Phone):

    def call(self):
        print(f"Calling from {self.brand} ...")

class Bank:

    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)
    
    def set_balance(self,amount):
        self.__balance +=amount

kotak = Bank("Tharun",1000)
kotak.get_balance()
kotak.set_balance(500)
kotak.get_balance()


from abc import ABC,abstractmethod

class Sim(ABC):

    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def call(self):
        pass

    def sms(self):
        print(f"SMS sent Successfully by {self.name}")

#s1 = Sim("jio")
#s1.sms()


class NegativeWithdraw(Exception):
    pass

balance = 1000

try:
    withdraw = int(input())
    if withdraw>balance:
        raise NegativeWithdraw("Insufficient funds")
except NegativeWithdraw as e:
    print("Error",e)
        

    




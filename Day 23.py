'''
polymorphism
:
polymorphism means many form.
it allows same method , function or operator to perform different
tasks depending on the same object.

types:
------------
1.method overloading
2.method overriding
3.operator overloading

1.method overloading:
_---------------------------
method overloading means having multiple methods with the same name but different parameters.


class cal:
    def add(self,num, num_2=0):
        print(num + num_2)
    def add(self,a,b):
        print(a+b)
obj = cal()
obj.add(4,7)
obj.add(45,75)

eg 2:
class cal:
    def add(self,num, num_2=0):
        print(num + num_2)
    def sub(self,a,b=0,c=0):
        print(a-b-c)
    def mul(self,a,b):
        print(a*b)
obj = cal()
obj.add(14,47)
obj.sub(45,15)
obj.mul(9,234)



#2.Method Overriding: the method overriding occurs when a child class provide its own implementation of
a method already defined in its parent class.

class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")
d = dog()
d.sound()


3.operator overloading:
this allows operators (+,-,*) to work differently for user-def onjects
methods:
1.__add__(+)
2.__sub__(-)
3.__mul__(*)


class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks


# Data Abstraction: Data Abstraction is the process of hiding implementation details and showing only the essential
data to the user.
#Data abstraction :
# Eg: ATM, CAR, APP

# Eg:

#from abc import ABC, abstractmethod

class parent:
    @abstractmethod
    def display(self):
        pass
s1 = student(56)
s2 = student(67)
print(s1 + s2)

eg 2:
from abc import ABC,abstractmethod

class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementatedError ('Subclass must implement interest()')

class SBI (bank):
    def interest(self):
        print('SBI interest Rate : 6.5%')

class HDFC (bank):
    def interest(self):
        print('HDFC interest Rate : 5.5%')

class ICIC (bank):
    def interest(self):
        print('ICIC interest Rate : 6.9%')

banks = [SBI(),HDFC(),ICIC()]

for j in banks:
    j.interest()
        
'''

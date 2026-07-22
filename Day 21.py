'''
#self keyword
-------------------------
self refers to current object.....
eg:
class Test:
    def display(self):
         print(self)
te = Test()
print(te)
te.display()


constuctor
-----------------
--> This constructor initializes the object automatically whn it is created...
eg 1:
class Batch:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print(self.name)
        print(self.branch)

b4 = Batch('Rama', 'CSE')
b4.display()

eg 2:
class fam:
    def __init__(self):
        self.name = "rudra"
f = fam()
print(f.name)

eg 3:
class bank:
    def __init__(self):
        self.__pin = '6000'
AC = bank()
print(AC._bank__pin)

eg 4:
class Bank:
    def __init__(self):
        self.__pin = '7700'
    def display(self):
        print(self.__pin)
ac = Bank()
ac.display()

#encapsulation: it means  wrapping the data and methods into a single unit(class) while contolling access to the data.



'''
class atm:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
        print(self._balance)

tran = atm(balance = int(input("Enter Amount :")))
tran.deposit(amount = int(input("Enter Amount:")))   

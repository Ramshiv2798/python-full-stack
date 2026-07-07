'''

                                DAY 12 - PYTHON FUNCTIONS

Functions:
-----------------
-> Function is a block of code that can be reusable
-> Function can avoid the repeated line of code...

Functions of 2 types:
-----------------------
1. built-in
---------------
ex: print(), max(), min(), type(), sum()

2. user-define
---------------
-> This function start with keyword (def)
syntax -> def func_name(parameters):
            ------------------------
            ------------------------
            ------------------------
         func_name(arguments)

ex:
    def add(a,b):
        print(a+b)
    add(3,4)

types of arguments:
--------------------
1.Required arguments:
----------------------
-> we have to pass same number argumnets with definition of the functions.
ex:
    def add(a,b):
        print(a+b)
    add(3) #error , beacause we have to give exact arguments like parameters
    
2.Default:
-----------
-> 
ex:
    num = 9
    num2 = 10
    def add(a,b):
        print(a)
    add(num,num2)

3.Keyword:
-----------
-> we can pass a pair like (variable = datatype)
ex:
    def add(a,b):
        print(a+b)
    add(a=9,b=10)

 
4.variable length:
-------------------
-> we can pass n number arguments and just use (*args) in the parameters, will recieve tuple of arguments, (**args) in parametes, will recieve dictionary of arguments
ex: --> (*args)
    num = 9
    num2 = 10
    num3 = 5
    def add(*a):
        print(a)
    add(num,num2,num3)

ex: --> (**args)
    def add(**a):
        print(a['name'])
    add(name = "ekanth", age = 21)

Global variable:
--------------------
-> we can use variable through out the program
ex:
    num = 9
    def func():
        print(num)
    func()
    print(num)

    num = 9
    def func():
        global num
        num = 89
        print(num)
    func()
    print(num)

note: -> to change the global variable by using keyword (global) that can change completely inside and outside of the function

Local variable:
--------------------
-> we can use variable only inside the function and not for throught out the program
ex:
    def func():
    num = 9
        print(num)
    func()
    print(num)
    

'''
    

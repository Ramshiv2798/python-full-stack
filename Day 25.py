'''
              Error Handling

SyntaxError:
------------------
#eg1:
for j in range(1,10:
        print(j)

o/p---SyntaxError


identation error
----------------
 a = 20
for j in range(a):
     print(j)
else:
print()

o/p ---- IndentationError

Value error
------

num = int(input("Enter a num:"))
o/p--ValueError

try
---------
the try block will test the code for error.

syntax: try:

except
---------
the except let us handle the errors in the code.
Syntax: except

else
finally

try:
    print(num)
except :
    print('Will get name error')

try:
    num = int(input("Enter a num: "))
except ValueError:
    print('Will get value error')

#else:
eg:
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num / num_2)
except ZeroDivisionError:
    print('will get zerodivision error')    
except ZeroDivisionqError:
    print('will get zerodivision error')
else:
    print('no error')


finally:    

try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num / num_2)
except ZeroDivisionError:
    print('will get zerodivision error')    
except ZeroDivisionqError:
    print('will get zerodivision error')
else:
    print('no error')

finally:
    print('end')
'''

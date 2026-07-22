'''


                    DAY 26 - PYTHON CONCEPTS

File Handling:
-----------------
File handler is an object that gives more options like creating, updating

two ways to open the file...
1.open():
----------
syntax --> do = open('file_name','mode')
           
ex:
do = open('demo.txt','r')
print(do.read())

2.with (keyword):
-----------------
syntax --> with open('file_name','mode') as do:

ex:
with open('demo.txt','r') as do:
    print(do.read())

Modes:
-------
r --> used to read the file, incase if the file is not present it will raise error.

w --> used to write the text inside the file

ex:
---
with open('dem.txt','w') as do:
    print(do.write('we are using file handling'))

a --> this is used to add the text at last position inside the file.

ex:
---
with open('dem.txt','a') as do:
    print(do.write('\nshankarooooooooooooooooo'))

x --> used to create a new by adding the inside the file, incase if the file is present it will raise an error......

ex:
---
with open('dem.txt','x') as do:
    print(do.write('\nshankarooooooooooooooooo'))

write()
--------
--> this function is used to add the text inside a file or update a file with new text....
ex:
---
with open('demo.txt','r') as do:
    print(do.write(10))


read():
--------
--> used to read a file and this read() will read file chunk by chunk
    we can also specify the size  
ex:
---
with open('demo.txt','r') as do:
    print(do.read(10))
    
readline():
------------
--> this readline() function will read only one line at a time...
ex:
----
with open('demo.txt','r') as do:
    print(do.readline(10))
    
readlines():
------------
--> this function will read whole file and give it in a list each line is one index in that list....
ex:
---
with open('demo.txt','r') as do:
    print(do.readlines())

'''
with open('demo.txt','r') as do:
    print(do.readline(10))



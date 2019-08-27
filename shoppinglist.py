import os
import sys
import json
sl = []

PATH_TO_MY_FILE = './shoppinglist.txt'

#nick is a fucking asshole

# oneitemdictionary = {item : "bread"}
# oneitemdictionary['item']
#https://stackoverflow.com/questions/17096631/lookuperror-unknown-encoding-cp0
#if we are going to make a class

text = """
    sl = [
    'item_0' : {
            'name' : 'fish'
            'quanity' : 2
            'price' : 3.00
            }
,
    'item_1' :{
            'name' : 'eggs'
            'quanity' : 1
            'price' : 2.59
            }    
sl = [{}, {}]

We want to have an array of objects because they all have itemized attributes
but are all the same!
item_0[']

    item_ + str(iterator)
        name - quanity - price 

    class Item:
        def __init__(self):
            self.name = '' 
            self.quanity = 0
            self.price = 0
"""

#obj = {'item_0': {'name': userinput[0], 'quantity': userinput[1], 'price' : userinput[2]}}

# obj1 ={'name': 'oranges', 'quantity': 3, 'price' : 4.00}
# obj2 ={'name': 'pickles', 'quantity': 72, 'price' : 2.50}
# obj3 ={'name': 'oranges', 'quantity': 3, 'price' : 4.00}
# obj4 ={'name': 'pickles', 'quantity': 72, 'price' : 2.50}
# sl = [obj1, obj2, obj3, obj4]
# for item in sl:
#     print('name: {}  | quantity {} | price {} '.format(item['name'], item['quantity'], item['price'])) 


#['fish', ' 2', ' 3.00']


def mainScreen():
    os.system('cls')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~shopping list~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("(a)dd something")
    print ("(d)elete something")
    print ("(c)lear all")
    print ("(v)iew list")
    print ("(l)oad")
    print ("(s)ave")

    print ("(q)uit")
    quickuser = input()
    return quickuser

def addScreen():
    os.system('cls')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~add screen~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('/n Add an item to the list in the formate /"name, quantity., price/"')
    print('Example: fish, 1, 3.00')
    obj = {}
    try:
        userinput = str( input() )
        uin = userinput.replace(' ', '').split(',')
        obj = {'name': uin[0], 'quantity': uin[1], 'price': uin[2]}
    except:
        print ("Can you please follow the pattern!!")   
        input() 
        
    return obj

    # you are returning an array now ex ['fish', '1', '3.00']

    
def viewScreen():
    os.system('cls')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~view screen~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    # for i, item in enumerate(sl):
    #     print(i, " ", item)
    subtotal = 0

    for item in sl:
        print('name: {} | quantity {} | price {} '.format(item['name'], item['quantity'], item['price']))
        subtotal = subtotal + ( int(item['quantity']) * float(item['price']) )
        
    print('\n\nSubtotal = \t\t\t${0:.2f}'.format(subtotal))
    print('Tax 7% = \t\t\t${0:.2f}'.format(subtotal * 0.07)) # https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    print('Total = \t\t\t${0:.2f}'.format(subtotal * 1.07))

    nothing = input()
    pass
    #print("{0:.2f}".format(a))
def deleteScreen():

    os.system('cls')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~Delete Screen~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for i, item in enumerate(sl):
        print(i, " ", item)

    return input()

def saveScreen():
        
    os.system('cls')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~Save Screen~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    # file = open.save(PATH_TO_MY_FILE)
    savefile = json.dumps(sl)
    file = open(PATH_TO_MY_FILE, "w")
    file.write(savefile)
    file.close()

    input()
    
    pass


def loadScreen():
        
    os.system('cls')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~Load Screen~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    

    file = open(PATH_TO_MY_FILE, "r")
    loadfile = json.load(file)
    

    input()

    return loadfile

    

done = False

if __name__ == "__main__":

    while (done == False): 

        userinput = mainScreen()

        if (userinput == "a"):
            sl.append(addScreen()) 

        if (userinput == "v"): 
            viewScreen()

        if (userinput == 'q'):
            break

        if (userinput == 'd'):
            deleteThisNumber = deleteScreen()
            if ( int(deleteThisNumber) > (len(sl) - 1)):
                print("you cannot enter a number great then the list's length")
                input()
            else: 
                del sl[int(deleteThisNumber)]               #https://www.programiz.com/python-programming/array
        if (userinput == "l"):
            sl = loadScreen()
        if (userinput == "s"):
            saveScreen()
         
            
# >>> for item in shoppingList:
# ...     print(item['name']
# ...     print(item['name'])
#   File "<stdin>", line 3
#     print(item['name'])
#         ^
# SyntaxError: invalid syntax
# >>> for item in shoppingList:
# ...     print(item['name'])
# ...
# fish
# eggs
# >>> for item in shoppingList:
# ...     print("name: {} ")
# ... for item in shoppingList:
#   File "<stdin>", line 3
#     for item in shoppingList:
#       ^
# SyntaxError: invalid syntax
# >>>     print("name: {} ")
#   File "<stdin>", line 1
#     print("name: {} ")
#     ^
# IndentationError: unexpected indent
# >>>
# >>> for item in shoppingList:
# ...     print("name: {} quanitiy")
# ... for item in shoppingList:

# Traceback (most recent call last):
#   File "c:\Python27\lib\encodings\cp437.py", line 14, in decode
#     def decode(self,input,errors='strict'):
# KeyboardInterrupt
# >>> for item in shoppingList:
# ...     print("name: {} quanitiy: {} price: {}".format(item['name'], item['quantity'], item['price'])  )
# ...
# name: fish quanitiy: 2 price: 3.0
# name: eggs quanitiy: 1 price: 2.59
# >>> for item in shoppingList:


#["eggs", "oranges", "lobster"]

# numbers = arr.array('i', [10, 11, 12, 12, 13])
# # numbers.remove(12)

# del number[2] # removing third element
# print(number) 


# # Here age is a string object
# age = "18"
# print(age)
# # Converting string to integer
# int_age = int(age)
# print(int_age)

#deleteThisNumber = ["oranges", "apples"]
#print (len(deleteThisNumber))  --- this gives 2


# to find the length of a array is 
# len(deleteThisNumber)


# set PYTHONPATH=%PYTHONPATH%;C:\Python27

# https://docs.python.org/2/using/windows.html

#https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/

# https://dev.to/el_joft/installing-pip-on-windows

# https://stackoverflow.com/questions/7604636/better-to-try-something-and-catch-the-exception-or-test-if-its-possible-first

# https://gist.github.com/keithweaver/4716b88f0b6e3e17577a819f42d348db
'''

Consider : Writing to a File


def writeToFile(path, content):
    file = open(path, "w")
    file.write(content)
    file.close()
  



PATH_TO_MY_FILE = './shoppinglist.txt'
CONTENT_FOR_MY_FILE = 'Example\nThis is on line 2 of a text file.\n\nThe end.'

writeToFile(PATH_TO_MY_FILE, CONTENT_FOR_MY_FILE)

https://docs.python.org/3/library/io.html

saying the same fuycking thing


with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')


     >>> 125650429603636838/(2**53)
  13.949999999999999

  >>> 234042163/(2**24)
  13.949999988079071

  >>> a=13.946
  >>> print(a)
  13.946
  >>> print("%.2f" % a)
  13.95
  >>> round(a,2)
  13.949999999999999
  >>> print("%.2f" % round(a,2))
  13.95
  >>> print("{0:.2f}".format(a))
  13.95
  >>> print("{0:.2f}".format(round(a,2)))
  13.95
  >>> print("{0:.15f}".format(round(a,2)))
  13.949999999999999

  

'''

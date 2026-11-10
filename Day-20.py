'''
OOP ---> Object Oriented Programming
POP ---> Procedure Oriented Programming
'''
#FUNCTIONS  
'''A function is a Block of Code (statements) which performs a specific task.It is a resuable Code.---->Readbility,Reuseability
and easy to maintain...
'''
#Types of Functrions:
'''
1)User Defined Functions---> def
2)Built-in Functions --->Python by default(print,len,min,max,sorted,str,list,bool....)
3)Anonymous Functions ---> Nameless Functions ---> Lamda(map,Filter) reduce
4)Recursive Functions --->Recursion --->Factorial,Fibonaccci--->Decorators
'''
#USER DEFINED FUNCTIONS:
'''
Syntax:
----------

def fname(parameters) :    #Function header
      """DOC String (Description of Function)"""
      statemennt(s).......   #Body of the function
      ................................
      return value(s)
fname(args)   #function call
'''
#Simple Function to understand the Reusability
'''
a=10
b=20
print(a+b)
'''

'''
def add(a,b):
    """This Function will returns the sum of the given objects"""
    c = a+b
    #print(c)
    return c

print(add(16,14))
add((1,2),(3,4))
print(add("bala","krishna"))
add([1,2],[3,4])
'''
#EX:
'''
def add(a,b):
    """ adding two numbers"""
    return f"sum of two numbers :{a+b}"
e,d=map(int,input().split())
print(add(e,d))
s,x=22,23
c=add(s,x)
print(c)
'''
#Functions are also Objects

def greetings():
    """ greetings to users"""
    return "hey balu", "welcome to Vizag"
     #return 24+26 #A function can have multiple values to return but not multiple return statements
print(greetings())

#print(greeting())
print(greetings() * 5)
print(type(greetings()))
print(type(greetings))


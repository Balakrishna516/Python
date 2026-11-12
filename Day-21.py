#fname(args) #actual arguments
'''
Positional aruguments ---> Count of arguments to be matched
Default arguments --->we can make arguments as default
keyword arguments ---> order/keyword name to be matched
Variable length arguments (*args) --> we can pass any number of postional
keyword variable lengths arguments (**KWARGS) --> we can pass any number of keyword arguments
'''

#POSITIONAL ARGUMENTS :---->Count of arguments to be matched
'''
def data(a,b,c):
    """Function to perform Arthematic Operations"""
    d=a+b+c
    e=a-b-c
    f=a*b*c
    g=a/b/c
    return d,e,f,g
print(data(12,3,1))
#print(data(23,1,)) #Type error as count is mismatched
#print(data(23,1,4,5,6)) #Type Error ----> takes only 3 arguments
d,e,f=map(int,input().split())
result =data(d,e,f)
print(f"result is :{result}")
'''
#DEFAULT ARGUMENTS ---> we can arguments as default
'''
def data(a,b=5,c=2): #non-default arguments always follows arguments 
    """Function to perform Arthematic Operations"""
    d=a+b+c
    e=a-b-c
    f=a*b*c
    g=a/b/c
    return d,e,f,g
print(data(2,4,6))
print(data(2)) #here we need not mention other arguments as they are default
print(data(2,4)) #here one default arguments taken
d=int(input())
result=data(d) #mandatory Count to be matched
print(f"result:{result}")
'''
#KEYWORD ARGUMENTS --->Key word name to be matched
#Grocery Purchase
'''
def grocery(item,price=90):
    """Useage of Keyword arguments"""
    print(f"item is :{item}")
    print(f"item value is :{price}")
grocery("pizza")
grocery("milk",35)
#grocery(40,"bread")  #in this case order differs result changes
grocery(price=40,item="Bread")
#grocery(items="jam",price=90) #TYPE_ERROR --->  got an unexpected keyword argument 'items'
'''
#VARIABLE LENGTH ARGUMENTS ----> we can capture any number of positional
#arguments,we can (*args),captures excess postional arguments and pack them into  tuple...

def sample(*a):
    """usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2)

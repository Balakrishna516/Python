#in above cases we used "*" to pack the values into tuple
'''
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c=2,4,5,6,7,-12
print(a)
print(c)
print(b) # in this case all values are stored into list
#a,*b,*c=2,4,5,6,-12 #Multiple expressions are not allowed..
'''
#find the sum of values:
'''
def add(*a):
    "usage of variable length arguments"
    print(a)
    print(type(a))
    result=0
    for value in a:
        result=result+value
    print(result)
#add()
add(1,3,4,5)
add(12,3,4,5,6,-98,12)
'''
#OR
'''
def add(*a):
    """usage of variable length arguments"""
    result=0
    for value in a:
        result=result+value
    return result
print(add(1,2,3))
'''
'''
def add(*a):
    """usage of the variable length arguments"""
    result=0
    for value in a:
        if type(value) == int or type(value) == float: #MEMBERSHIP OPERATOR
            
            result=result+value
            #print(result)
    return result       
print(add(1,2,3,"balu",-4,8,"coder",9))
'''
#What if we accept the group of values
'''
def add (*a):
    """usage of the variable arguments"""
    result=0
    for value in a:
        if type(value) == int or type(value) == float:
            result=result+value
    return result
d= list(map(int,input().split()))
print(d)
print(add(*d)) #we need to use * to unpack the values from the tuple
'''
#we will use above usage of varibale length arguments for ordering pizza
'''
def order_pizza(size,*toppings):
    """usage of *args"""
    print(f"size of pizza:{size}")
    print(f"Toppings:{toppings}")
    for topping in toppings:
        print(f"topping added:{topping}")
order_pizza("large","onions","capsicum","carrot","mushrooms")
'''
#keyword variable length arguments :ANY number of keyword arguments,data is stored in dictionary,we use **KWARGS
'''
def sample(**a):
    """usage of the **KWARGS"""
    print(a)
    print(type(a))
sample()
sample(name="balu",batch="PFS-VSP-007",place="vskp",branch="cse")
'''
def order_pizza(size,*toppings,**details):
    """usage of *args"""
    print(f"size of pizza:{size}")
    print(f"Toppings:{toppings}")
    for topping in toppings:
        print(f"topping added:{topping}")
        for key,value in details.items():
            print(f"data is {key},result is {value}")
order_pizza("large","onions","capsicum","carrot","mushrooms",
            name="balu",
            bill=700,delivery=False,tip=100)

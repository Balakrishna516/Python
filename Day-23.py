#Use of varible length and keyword varible lenght arguments
'''
def scores(branch='Codegnan',*marks,**names):
    """scores scenrio with varible and keyword varible lenght arg"""
    print(marks)
    print(names)
    total=0
    for mark in marks:
        if type(mark) in (int,float):
            total +=mark
    print(f'Total Marks are : {total}')
    #for name in name.values():
    for name,value in names.items():
        print(f'Name : {name}')
        print(f'Values : {value}')
        print(f'Branch :{branch}')

scores(28,34,30,87,33,names='Deepak',place='Vizag',batch='PFS-VSP-007')
'''

#scope ---> Determins where a varible can be accessed within a program
#A Varible is only accessible within th region where it is defined....

'''
Types of scope-->
1. Local Scope
2. Global socpe
3. Global Keyword
4. NonLocal Scope
'''
#Local Scope --> Vribles defined and accessible only inside the function...
'''
def fname():
    """Usage of Local Varible"""
    name ="Codegnan"
    return f'{name} is in Vizag'
print(fname())
#print(fname(name='Deepak')) it will typeerror because the keyword arg was not define
name='Deepak'
print(name)  # it will give the print it not in function
'''

#Global Varible---> A Varible declared outside all function  is called a global Vrible.
#It can be accessed from anywhere in the program.
'''    
name="Codegnan"
def uname():
    """Global scope"""
    #name='Deepak'  Local Varible get heigher priority inside the functino
    return f'{name} is in Vizag,Vijayada and HYD.'
print(uname())
print(name)
'''

#Global Keyword---> Used when we to modify a global varible
#inside the function
'''
count=15
print(f'old count={count}')
def update():
    """Global Keyword"""
    global count
    count=count+5
    return f'Update count is {count}'
print(update())
print(count)
values=[1,2,3,4]
values.append(count)
print(values)
'''

#NonLocal Scope--> Used in Nested Function ... Allows Modificatios of varibles from the outer function
'''
def outer():
    count=12
    def inner():
        nonlocal count
        count=count+5
        return f'result from Inner function is {count}'
    print(inner())
    return f'Result from Outer function is {count}'
print(outer())


#LEGB rule--> Local,Enclosing--> Global-->Built-in
len=45
a=['Codegnan','Deepak']
# print(len(a)) here it is error we ha

'''

#Function are termed as first class Objects

#pass by value and Pass by object reference

#Pass by value -->
# int,float,bool,str,tuple,complex,frozensets
#when immutable objects aer passed to function, changes inside the function donot effect the original value

def update(number):
    """Pass By Value usage"""
    number=15
    print("Inside function:",number)
number=20
update(number)
print("Ounter value",number)














































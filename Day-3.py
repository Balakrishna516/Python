"""
Datatypes --> it will tell us how to define the data

Numeric Datatypes --->integer,float,complex
Boolen type ---> True/False
None type ---->None
Sequence types ---> STrings,lists,sets,frozensets,mappings(dictonaries)
"""
#Numeric datatypes --> Integer --->quantities,ids,orderids,stock,age --->Int
"""
age=32
print(age)
print(type(age))
stock =35
print(type(stock))
rollno =516
print(rollno)
print(type(rollno))
"""
#float Values -->salaries,price,percentage,temp ----->Float
#Eg:-
"""
salary =30000.5
print(salary)
print(type(salary))
"""
#Complex -->real and imaginary values --->scientific calcns,signal processing
#Eg:--
"""
data=3+7j
print(data)
print(type(data))
"""

#Boolean -->True/False ---->Validations
#Eg:-
"""
access=True
print(type(access))
balu=False
print(type(balu))
"""
#Nonetype ---> None
#None -->0,False,' ',{},[],(),set() ----->None cases in python
#Eg:--
"""
branch_rank = None
print(type(branch_rank))
"""
#Typeconversion -->Converting one datatype to another datatype
#explicit conversion

#Integer --->Float,complex,boolean
#Every built-in datatype is a built-in function

#Eg---->
'''
rank = 5
print(type(rank))
b = float(rank)
print(b)
print(type(b))
c =complex()
print(c)
print(type(c))
d= bool(rank) #bool(anything) is True,bool
print(d)
print(type(d))
ranks=0
e=bool(ranks)
print(e)
print(type(e))
#Space is also a character
print(bool([' '])) #empty string inside a list'''

#Float ---> Integer,Complex,Boolean
'''
a=16.6
print(type(a))
b=bool(a)
print(b)
c=int(a)
print(c)
d=complex(a)
print(d)
'''
#Complex ---> int,float,bool
'''
s=5+6j
#c=int(s)
#raises typeerror (invalid datatype)
#print(c)
#d=float(s)
e=bool(s)
print(e)
'''
#Boolean ---->int,complex,float
'''
access=True
b=int(access)
print(b)
c=complex(access)
print(c)
f=float(access)
print(f)
'''
'''
a=int(float(bool(5)))
print(a)
b=bool(float(int(516))) #check for the outer one
print(b)

c=True+35+3.5+(6+5j) #True becomes 1
print(c)
'''
#Sequence Types ---> strings,lists,sets,frozensets,dictionaries
#Strings ---->Group of characters
#quotations --->single,double,triple quotes
name="BALA KRISHNA"
print(type(name))
print(name)
#Strings are immutable,Ordered,Indexed Collections
print(len(name)) #len(obj) -->returns the number of items in a collection
print(len('vizag'))

#Space is also a character
a=" "
b=""
print(a)
print(len(a))
print(len(b))
#print(float(course)) it will show you error
print(bool(name))

#int -->str
#Float -->str
#complex --->str
#bool --->str
data =56
b=str(data) #it becomes numeric string
print(b)
m=13.5
c=str(m)
print(type(c))
d=str(5+3j)
print(d)

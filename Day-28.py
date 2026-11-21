#Multiplication table pattern
'''
data = [[i*j for i in range (1,11)] for j in range(1,11)]
#print(data)
for i in data:
    print(*i)
'''

#OUTPUT
'''
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100
'''
#Nested Comprehension  with if condition
#Syntax :[Expression for i in iterable1 for j in iterable2 if condition]
#Possible pairs without matching values
'''
data =[(i,j) for i in range (1,4) for j in range(1,4) if i!=j]
print(data)

f=[i*j for i in range (1,4) for j in range (1,4) if i!=j]
print(f)
print(*f)
'''

#output:
'''
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
[2, 3, 2, 6, 3, 6]
2 3 2 6 3 6
'''

#Nested Comprehension with if-else usage
#[true _value if condition else false-value
#For item1 in iterable1 for item2 in iterable2]
'''
week_1=[15,20,25,22,18,19]
week_2=[23,19,25,18,19,25]

result=['improved' if x<y else "lagged" for x in week_1 for y in week_2]
print(result)
'''

#OUTPUT:
'''
['improved', 'improved', 'improved', 'improved',
 'improved', 'improved', 'improved',
 'lagged', 'improved', 'lagged', 'lagged', 'improved', 'lagged',
 'lagged', 'lagged', 'lagged', 'lagged', 'lagged', 'improved', 'lagged', 'improved',
 'lagged', 'lagged', 'improved', 'improved', 'improved', 'improved', 'lagged', 'improved',
 'improved', 'improved', 'lagged', 'improved', 'lagged', 'lagged', 'improved']
'''
#make sure to check the braces and closures
#In the above  case if we replace [] braces with ()---> we dont get tuple

#generators
'''
week_1=[15,20,25,22,18,19]
week_2=[23,19,25,18,19,25]
result=('improved' if x<y else "lagged" for x in week_1 for y in week_2)
print(result)
'''

#OUTPUT:
'''
<generator object <genexpr> at 0x0000025ABFE3E0A0>
'''

#GENERATOR  --->IT is a Special Function,Which produces one value at a time
#we use yield Keyword
'''
def fname():
    """Doc string"""
    return value(s)
fname()

def fname():
    """DOC string"""
    yield value1
    yield value2
    yield value3
fname()
def func():
    """Normal Function"""
    return[1,2,3,4,5]
    #return "Saketh" # A function can have return with multiple values
#print(func())
data = func()
for i in data:
    print(i)
'''
'''
def func():
    """Generator Function"""
    yield 1
    yield 2
    yield 3
#print(func())
b = func()
print(next(b))
print(next(b))
print(next(b))
'''
#print(next(b)) it raises StopIteration as values are already Fetched
'''
def display():
    """Subjects Covered"""
    yield "python"
    yield "Aptitude"
    yield"Softskills"
    yield"Frontend"
    yield"FastApi"
print(display())
g=display()
print(f"subjects alloted is {next(g)}")
print(f"subjects alloted is {next(g)}")
print(f"subjects alloted is {next(g)}")
print(f"subjects alloted is {next(g)}")
'''
'''
week_1 = [15,20,25,29,28,30]
week_2 = [24,25,28,29,21,22]
result = ("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
#print(result) #it returns a generator
g = result
print(next(g))
print(next(g))
print(next(g)) #next function will fetch the value from the generator
print(*result)
'''
#Exception Handling ---->It is the mechanism in the python to respond to
#Runtime Errors or Exceptions
#Exception is an event that occurs during the execution of a program
#which disrupts its normal flow...

#TypeError,ValueError,IndexError,AttributeError,KeyError,ZeroDivisionError.

#We will be using try,Except and finally
'''
Syntax:
try: #You write code which may cause an error
       #Code that raises an expection
except ExceptionType: #it handles the error if it occurs
        #Code to handle the Exception
'''

#Basic Exception Handling
'''
a,b=5,3
try:
    result =a/b
    print(result)
except Exception as e:
    print(e)
'''
#a,b = map(int,input("Enter the values:").split())
#print(a,b)
'''
try:
    a,b = map(int,input("Enter the values:").split())
    print(a,b)
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')
'''
#OUTPUT:
'''
    Enter the values:45 13
45 13
Answer is 3.4615384615384617
'''
#Multiple except Blocks
'''
try:
    a,b = map(int,input("enter the values:").split())
    #print(a,b)
    result = a/b
    print(f"answer is {result}")
except ValueError:
    print("values should not be only 2 and only integers")
except ZeroDivisionError:
    print("cannot be divide by")
except NameError:
    print("improper")
'''
#OUTPUT:
'''
enter the values:345 1444 
answer is 0.2389196675900277
'''
'''
try:
    subjects=["python",45,"AI",30]
    #print(subjects[5])
    subjects.append("sql")
    print(subjects)
except Exception as e: #this can be written if u want exception to take care
    print(e)
except IndexError:
    print("make sure to check the length of the list")
except NameError:
    print("checking spelling")
except AttributeError:
    print("Check the method properly")
finally:
    print("anyway this was be printed")
'''
#output:
'''
['python', 45, 'AI', 30, 'sql']
anyway this was be printed
'''
#Catching Multiple Exceptions Together
'''
try:
    value=int(input("enter the value:"))
    #result = 10/value check this case
    f=10/value
    print(f)
except (ValueError ,ZeroDivisionError,NameError) as e:
    print(f"An error Occured:{e}")
'''   
#output:
'''
enter the value:12
0.8333333333333334
'''
#RAISING EXCEPTIONS
#YOU can raise exceptions intentionally using raise Keyword
'''
value=15
if value <0:
    raise ValueError("value can not be negativea")
#else:
#      print("done")

Custom Error Messages:
try:
    raise Exception("custom Error Message")
except Exception as e:
    print(e)
'''
'''
try:
    value=-15
    if value <0 or value in[1,20]:
        raise Exception ("value cannot be  negative")
except Exception as e:
    print(e)
'''
'''
def fn(a,b):
    """testing"""
    return a*b
print(fn(50,20))
'''
#OUTPUT:
'''
1000
'''
    
    
    

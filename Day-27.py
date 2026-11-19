'''
Reduce () ---> It reduces an iterable into a single value..It
repeatedly applies a function to combine elements..

we can use it from functools
syntax---> reduce(function,iterable)
'''

import functools
from functools import reduce
#Sum of numbers from a iterable
'''
numbers = [1,5,2,3,4]
result =reduce(lambda a,b:a+b,numbers)
print(result)
'''
#Multiplication of numbers from a iterable
'''
numbers=[1,5,2,3,4]
result=reduce(lambda a,b:a*b,numbers)
print(result)
'''
#Largest number from a collection
'''
data=list(map(int,input().split()))
print(data)
result = reduce (lambda a,b:a if a>b else b,data)
print(result)
'''
#returns the longest word in a group of strings
'''
words=["pyhton","developer","sql","programming"]
longest= reduce(lambda a,b: a if len(a) >len(b) else b,words)
print(longest)
'''

#Map--->Transformation
#Reduce---->Aggregation
#Filter------>selection

#List comprehensions ----->In python,it is a precise way to create
#Lists
#Syntax --->[Expression for item in Iterable]
#Iterable -->list,set,dict or range()
'''
li =[]
for i in range(10):
    li.append(i)
print(li)

li = [i for i in range(10)]
print(li)
'''

#SQUARES of 1-10 numbers in a list
'''
squares =[i**2 for i in range(1,11)]
print(squares)
'''

#EVEN numbers of 1-10 numbers in a list
'''
even=[i for i in range(1,11) if i%2==0]
print(even)
'''

#ODD numbers of 1-10 numbers in a list
'''
odd=[i for i in range(1,11) if i%2!=0]
print(odd)
'''
#Update scores of each person with 10 marks
'''
scores=[25,45,65,79,90]
f_scores=[i+10 for i in scores]
print(f_scores)
'''
'''
m_scores=list(map(lambda i:i+10,scores))
print(m_scores)
'''
#List Comprehension with if -else usage
#[true_value if condition else false_value fro item in iterable]
'''
data=[12,4,5,6,8,9]
result =["even" if i%2==0 else "odd" for i in data]
print(result)
'''
'''
result = [i**2 if i%2==0 else i**3 for i in data]
print(result)
'''
#nested List comprehensions --> One inside another
#[expression for i in iterable1 for j in iterable2]
'''
colors = ['Red','Blue','White']
sizes = ['S','M','L','XL']
dress = [(color,size) for color in colors for size in sizes]
print(dress)
'''
'''
d=[(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
'''
print(*d)

              

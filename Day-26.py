'''
Functions are termed as First Class Objects....

Anonymous Functions : an Anonymous function is a nameless Function,we use lamda keyword to use it..

They are generally used for short simple, operations csn be written in a single line .They are also termed as Lamda functions...
They are generally used with filter(),map() and reduce()

Syntax: Lambda argument(s) : expression
'''
#create a function to get the area of rectangle
'''
def rectangle (l,b):
    """Area of Rectangle"""
    return l*b
print(rectangle(7,5))

area=lambda l,b :l*b
print(f"area of rectangle:{area(7,7)}")
'''
#SQUARE of the number --->Normal Function ---> lambda Function
'''
def square(number):
    """SQuare of the number"""
    return number ** 2
#print(square(9))
number = int(input())
print(f"square of the {number} is {square(number)}")

number=int(input())
square=lambda number:number**2
print(f"square of the {number} is {square(number)}")
'''
#Find MAXIMUM of the two numbers
'''

def maximum(a,b):
    """maximum of the numbers"""
    return a if a>b else b
print(f"maximum of the two numbers is :{maximum(10,42)}")

maximum = lambda a,b : a if a>b else b
print(maximum(10,1))
'''
#NO Parameters
'''
greet=lambda :"welcome to Vizag"
print(greet())
'''
#FILTER() used to select elements from an iterable based on a condition
#only the elements that satisify the condition are returned

#filter(function,iterable)

numbers = [1,2,4,6,7,8,9,10,12,45,67]
#Even numbers --->[2,4,6,8,10,12]
'''
def filter(lst):
    lst1=[]
    for i in lst:
        if i%2==0:
            lst1.append(i)
    return lst1
lst=list(map(int,input("Enter The list: ").split()))
print(filter(lst))
'''
'''
result =list(filter(lambda  num:num%2==0,numbers))
print(result)
'''
'''
odd_result=list(filter(lambda num:num%2!=0,numbers))
print(odd_result)
'''
'''
prices =[500,650,790,780,800]
#product price above 700
result=list(filter(lambda price:price>700,prices))
print(result)
'''
#MAP() applies transformation to every element in a collection
#MAP(functions, * Iterables)
'''
scores = [15,20,19,23]
result =list(map(lambda new_score:new_score+1,scores))
print(result)

d=list(map(int(input().split())))
print(d)
'''
#ADD GST --->18%
'''
prices =[1000,5000,4500]
final_price=list(map(lambda price :price +(price*0.18),prices))
print(final_price)
'''

#cal length of the objects in a collection
sub=["python","sql","softskills","aptitude"]
result=list(map(lambda subject:len(subject),sub))
print(result)

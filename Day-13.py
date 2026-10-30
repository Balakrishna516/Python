'''
Tokens -->Operators--> datatypes (Numeric, boolean, sequences--->str,lists,Tuples,sets,frozensets,dicts)

Control statements ---> These are the statemnets which makes the programming flow to be possible .They control the entire
flow of the program
---->When  to Execute,what to execute, how to Execute
------>Conditional statements --->If,Else,Elif
------>Jumping statements --->Break,Continue,Pass
assert,TRY,ExCEpt,finally
---->Repetition statements (Loops) ----> For,While
'''

#Conditional Statements --->Statements rely on the condition
'''
Syntax If :

if <Condition>:
      statements(s).....
      ....

data=True
if data:
    print("balu is a good boy")
    print("he is the best player")
#or
name = False
if name:
    print("balu")
print("balakrishna")

Rainy=True
#Rainy=False
if Rainy:
    print("it is raining out side")
print("it is sunny outside")


A=21
A=int(input("enter the value:"))
AB=[20,21,27,29]
if A in AB:
    print("A successfully Fecthed")
    print(f"AB are in {A}")
print(f"it is not presented in list")    

product =int(input("enter the product Number:"))
Total_products =50
if product <Total_products:
    print("product are present in the store")
print(F"product is avaliable in store")
 
product =int(input("enter the product Number:"))
Total_products =100
if product >0 and product <Total_products:
    print("product are present in the store")
print(F"product is avaliable in store")
'''

#Usage of Else:
'''
IF<condition>:
    statement(s)...
Else:
    statements
    
#True
#wheater =False
if wheater:
    print("it is sunny")
else:
    print("it is Cloudy")
'''
'''
Algo:
accept the input from the user
make the eligibility case as age greater thanequal to 18:
      Eligibilty Granted
if age is not matching eligibilty:
       Inform number of years to wait
DRY RUN :
age ---> 19 ---> result  ---> 19>18 and 19>0
age ---> 12 ----> result --> 18-12 and 6
age --> -12 ---> result ---->18-(-12) --->30
age= int(input("enter the age:"))
'''
#Code
'''
age= int(input("enter the age:"))
if age  >18:
    if age>0:
        print("he is Eligible for Vote")
    else:
       print("he is not Eligible for Vote")
       print(f"you have to wait {18-age} years to get eligibilty")
else:
    print("he is giving an unvalidate age")
'''
#or
'''
age = int(input("enter the age:"))
if age >0:
    if age >0 and age >=18:
        print(f"you have eligible to vote")
    else:
         print(f"you need to wait for {18-age} years")
else:
    print("you have entered the incorrect value")
 '''
#if-elif-else ---> we wanted to map multiple conditions
'''
if condition1:
    statements(s)...
elif condition2:
     statements(s)...
else condition3:
      statements(s)...

age =int(input("enter the age:"))
if age >18:
    print(F"you have eligible to vote")
elif age >0:
    print(f"you need to wait for {18-age} years")
else:
    print("you have entered the incorrect value")
'''
#Task is to built  ---> Placement Eligibilty TRacker/System
print("######Placement Eligibilty Checker######")
name = input("enter the name:")
attendance = float(input("enterv the attendance:"))
technical_score = float(input("enter the score:"))
mock_interview_score = float(input("enter the mock score:"))
projects = int(input("enter the number of projects:"))

avg_score = (technical_score + mock_interview_score)/2

if attendance >=75 and avg_score >=75 and projects >2:
    print(f"result : student is eligible for placements to apply for the jobs")
elif attendance >=60 and avg_score >=60 and projects<=2:
    print(f"result : student need more preparation ---> improvement stage")
else :
    print(f"result : student is in foundation stage ---> needs improvement")



    

    
    

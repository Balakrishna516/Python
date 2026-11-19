'''
Built-in Function--> Function which are inbuiltin python
abs(),an(),all(),bin(),bool....

dir(_builtins_)--->enumerate(),zip()

details=['Codegnan','Saketh','PFS-VSP-007']

0 : Codegnan
1 : Saketh
3 : PFS-VSP-007

for i in details:
    print(details.index(i),':',i)
    #or
for i in range(len(details)):
    print(i,':',details[i])
    
#enumerate() will create a counter objects for an iterable

#or
for i,j in list(enumerate(details)):  # we can use the enumerate function insted of for loop
    print(f'{i} : {j}')
'''
#zip() will combine multiple iterable into a single iterable
'''
data=['Ajay','Sai','Sanjay']
marks=(20,25,24)
detail=dict(zip(data,marks)) #if we take one more iterable it raises ValueError
print(detail)

emails=input().split()
print(emails)
for email in emails:
    print(email.split('@')[1])


#eval()--> You can take any input-->dict
salaries=eval(input("Enter the salaries :"))
print(salaries)
print(type(salaries))

print(int(4.65))
print(round(2.56)) #it will round of to next decimals
print(round(4.3892322,2))
'''
'''
Function is termed as first class object
Recursive function--->A function calling itself,
where it makes the smaller problem is broken into multiple times...
depends on two cases--> Based it indicates when to stop recursion)
-->Recursive case (it make the problem to be repeated

Syntax-->
def function():
    if base_condition:
        return
    function()  we write our recursive
function()
'''
#Factorial of n-->
'''
def fact(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "No -ve value onlye ve value only"
    else:
        return n*fact(n-1)

n=int(input("enter the factorial u need:"))
print(fact(n))
'''
#Sum of Natural Number using recursive logic-->

def sum(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "No -ve value onlye ve value only"
    else:
        return n+sum(n-1)

n=int(input("enter the factorial u need:"))
print(sum(n))






































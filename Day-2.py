#this is my first day of learning python
name="Bala Krishna"
age= 22
place="etikoppaka"
email_id="balakrishnauddandam@gmail.com"
#snakecase covenctions we use underscores for combine(multiple words)
'''1course_pfs7=vizag it will show error because we cannot assign any numbers are any key words
in the python at the begining'''
"""print(name)
print(age)
print(place)
print(email_id)
true=45#as True is a keyword we cannot use a variable
print(true)
#comments--->It will make users understand what if it conveying
#single line comment--->#
#multi line comments --->we can use triple quotes (doc string)

#multiassignment of variables
#make sure to pass same number of values

name,email_id,mobile,gender="Bala Krishna","balakrishnauddandam@gmail.com",8074028533,"male"
print(name,mobile)

#python by default follows implicit type(user need not allow)


#so u can prefer single line or multiple lines for assigning variables
name="balu";age=9;place="vizag"
print(name,age)

#Deletion --> del
del age #permanent deletion
del name,place
print(age)


#swapping of variables
a,b=25,10
print(a)
print(b)
a,b=b,a   #value of a will become b
print(a)
print(b)
c=a     #reassing the exisiting value to a new variable
print(c)
"""
#litterals--> these are constants such as numbers(int,float,complex)
age=35.5
print(age)
taste ="bad"
print(taste)
price =200
print(type(age)) #it returns the type of objects
#type() is very very imp

#Identifiers -->names given to a variables,functions,classes,objects,modules

#punctuators -->[ ] --->Lists,( ) --->Tuples,{ }---->Dictionaries,Sets

#Operators --->There are different type of operators -->operations
#+,-,*,**,/ (arithematic operators),//,%
a=5
b=3
print(a/b) #--->Float Divison (answer is always in float value)
print(a//b) # -->Flooring Division (Integer division) returns quotient
print(a%b)# Modulus --> returns remainder

#Raju purchased shoes with price 1000,discount 15%,
#Show how much raju has to pay?
price=1000
discount=0.15
final_price =price-(price*discount)
print(final_price)

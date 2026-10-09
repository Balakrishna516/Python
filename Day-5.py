'''
OPerators --->Operators help us to perform operations b/w operands

Airthmetic operators --->+,-,*,/,**,//(Integer or Floor division)
%(modulus ---> remainder)

Assignment operators ---> It helps us to  assign, update (increment), decrement values
# = (assigning) , += (addition&assign) ,-=(subtraction&Assign),
# *=(Multiplications&Assign) /=,//=,**=,%=

data =20
print(data)
print(type(data))
stock =data
print(stock)

#increment the value of stock
stock=stock+5 #stock+=5
print(stock)
print(data)

#decrement the value of the data by values
data=20
stock=25
data=data-2
print(data)
data*=3
print(data)
data/=5
print(data)
data//=2
print(data)
data%=4
print(data)
data**=2
print(data)


#Comparision Operators (Relational Operators) ----> It Performs comparsion
#between the operands and results in boolean True/False --->Conditions
# == , != , < , >,<=,>=
Name='Balu'
attendance =75
print (attendance ==80)
print (attendance >80)
print (attendance<80)
print (attendance<=80)
print (attendance>=80)
print (attendance !=80)


#Logical operators ---> And , OR ,NOT (keywords)
#AND ----> it needs all conditions to be satisfied (two are more) ---->True
#OR -----> it needs any condition to be satisfied 
#not ----> opp to existing
max_marks =80
balu_marks =75
max_att=75
balu_att= 70
balu_marks +=10
certificate =balu_marks >= max_marks and balu_att>=max_att
print(certificate)
chance =balu_marks >= max_marks or balu_att >=max_att
print(chance)
data=[]
print(data)
print(not(data))  #returns true
data=(1,2,3,4)
print(data)
print(not(data)) #returns false as data is existing
#Both logical & comparison operators will return result in Boolean

#Membership Operators --> IN,NOT IN
#check for the existances in a sequence (str,list,tuple,dict)


names=['vinay','vijay','balu','raju']
name='nikil'
print(name in names) #returns false
print(name not in names) #returns True
print('12' in '121')
#print(12 in 121) #type error as we have taken int type

print('a' in 'a') #retuns true as we are checking type as string
print(['a' ]in ['a']) #returns FALSE as its a list


#Identity Operators ---> it specifically refers to an object (memory locations
#ID ---> is,is not
a=15
b=15
print(a==b)
print(id(a))
print(id(b))
c=a
print(id(c))

print(c is a) #as id of both a and c are same --->type

a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(id(a))
print(id (b))
#as we have taken two lists evenhtough with smaller values identity
print(a is b)
c = a
print(id(c))
print(c is a) # returns true as we are assigning same object

a =(1,2,3)
b=(1,2,3)
print(a is b)
print(id(a),id(b))
#when we check with the interpreter mode and scripting mode above
#Tuples result changes

#Logical,membership,identity,Comparison(relational) --->always result is in bolean

#Bitwise Operators ---->
#It performs bitwise operations --> &(bitwise and)
#| (bitwise Or),^(bitwise XOR)
#AN integer will be converted  binary format and performs bitwise operation
#following integer to binary coversion
print(7&3)
print(7|3)
print(7^3) #XOR operation it returns 4
#7 to binary --->011
#3 to binary -->0011
#7^3 ---> 0100

#Shifting Operators(<<,>>)
print(7 << 1)
# 7<<1 actual 7= 0111
#after 7= 1110
'''

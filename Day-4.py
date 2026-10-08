'''
sequences --->str,lists[],tuples(),sets set(),mappings (dictionaries)
{},frozenset
'''
#lists  --> A list is an ordered,mutable,indexed and hetrogeneous collection
#we use [] to represent lists
#students details,order details,stock entries...
details=[1,'balu','pfs7','vizag',16]
#print(len(details))
#print(type(details))

std_id=['pfs01','pfs02','pfs03']
#print(len(std_id))
#print(std_id[1])
#print(std_id[2])
#print(std_id[-3])
std_id[0]='codegnan' #here we are using indexing
#print(std_id[0])

'''
#Tuples ----> () --> Tuples are also immutable,ordered,indexed and hetrogeneous
#Collections,we use ( ) paranthesis
#dimensions,coordinates

places =('hyd','viz','vjw')
#print(places)
#print(type(places))
#print(len(places))
#places[0]='ekp' #here we gained an error because we can not modified an exsisted tuples
#print(places)
#print(type(places))

a=10,20,30 #by default it becomes tuple
print(type(a))
print(a)

#Sets ---> A Set is a unique collection (removes duplicates)
#A Set is an unordered, Undiexed,Mutable collection
A =set()
print(A)
A=set([1,2,3,4,3])
B=set((2,4,6,4,2))
print(A,B)
c={'pfs','java','ds'}
print(c)
print(type(c))
#print(c[0]) ---->as set is unordered there is no index


#Dictionaries --- >A dictionaries (mapping object) is a collection of
#key values pairs ---> dict ={k:V} we access only by keys (indexed by keys)
#Dictionaries is also mutable collection

details ={'branch':'vskp',
               'batch':['pfs-007','pfs-006','pfs-005','pfs-004'],
               'course':'pfs',
               'count':19}
print(details)
print(type(details))
print(len(details))
print(details['batch']) #we access by giving only keys

id_s={'name':'BALU',
           'age':23,
            'phone_no':8074028533}
print(id_s)
print(type(id_s))

#evrey built in datatypes is a built-in function
#int,float,str,complex,bool,list,tuple,dict,set
#Lists --->tuples,sets,dict
marks=[35,24,54]
a=tuple(marks)
print(a)
b=set (marks)
print(b)

A=(1,2,3,4,2)
B=set(A)
print(B)

marks=[35,24,54]
#d= dict(marks) #its not possible like this
e=dict.fromkeys(marks) #we need to use from.keys (); whatever elements we have
#taken will become keys and valuses will be none
print(e)

#tuple --> list,set,str,dict
#Sets --->lsit,tuple,str,dict

#dictionaries --->lists,tuples,sets
ids = {1:12,2:34}
a=list(ids) #it will only fetch keys
print(a)
b=tuple(ids)
print(b)
c=set(ids)
print(c)
d=str(ids) #every symbol/objects will be a character
print(d)
print(len(d))

#Frozensets --->It is an immutable set
a=frozenset((12,32,12,32))
print(a)
print(type(a))
print(len(a))
b=list(a)
print(b)
c=tuple(a)
d=set(a)
e=dict.fromkeys(a)
f=str(a) 
print(c,d,e,f)
print(len(f))

A='BALA KRISHNA'
b=list(A)
c=tuple(A)
d=set(A)
e=dict.fromkeys(A)
print(b,c,d,e)
'''
#Operators --->Arthematic operators,Assignment,Comparision,
#Logical,MeMbership,Identity,Bitwise operators

#Arthematic --->*,+,-,/(floar division),//(Floor Divison) quotient
#% modulas(remainder),**(Expoentital)
a=3
b=2
print(a+b)
print(a-b)
print(a%b)
print(a**b)
print(a*b)
print(a/b)
print(a//b)




'''
Sets ---> A set is an unordered,unindexed collection,allow unique values,
Hetrogeneous Collection ,Mutable Collection

#A set   Can Contain only tuples in it but not lists,sets...
we can set() or adta inside {} braces

#Every Built-in datatype is a built-in function
#Subjects = {} #by default it will be empty dictionary
subjects=set()
print(type(subjects))
data=["python","MYSQL","aptitude","ss"]
subjects =set(data)
print(subjects)
print(len(subjects))

ids = {123,125,124,[1,2,3,"b"]} TypeError

#Set properties --> Membership
print (123 in {123,124,125})
ids = {123,121,125}
new_ids = {126,127}
#total = ids + new_ids #TypeError
#print(total)


#SEt is a Mutable collection -->Methods --->Insertion,Deletion along
#with mathematical set opertations
#ADD () --->Inserts single element to the set (UNique Values)

marks = {45,25,29,20,21}

print(type(marks))
print(len(marks))
marks.add(250)
print(marks)
print(len(marks))

#marks.add([1,2,3,4]) #it will raise an error
#print(marks)
d_marks = [10,5,3,4,6]
marks.update(marks) #upadate the set within itself or can take other sequence 
print(marks)
print(len(d_marks))
marks.update("codegnan")
print(marks)
print(len(marks))

marks = {45,25,29,20,21}
#marks.update(1,2,34) #TypeError

#Remove(),Discard ,POP()
print(marks.remove(45))
print(marks)
#Print (marks.remove(4)) #remove will  remove the object if existing else
#raises Keyerror
#discard() removes an element from set if existing if not it overrides
#The Error

print(marks.discard(20))
print(marks)

print(marks.discard(3))

#POP() will removes and returns an arbitrary  element from set 
print(marks.pop())
print(marks.pop())
print(marks.pop())
#print(marks.pop()) #returns the keyerror as set has become empty

#clear() ---> removes all elements and returns an empty set
marks ={1,2,3,4}
print(marks)
print(marks.clear())


#Mathematical set operations ---> Union(),Intersection(), Difference()...
a1 = {1,2,3,4}
a2 = {5,1,2,3}
a3 = a1.union(a2)
print(a3)
print(len(a3))
a4 = a1 | a2
print(a4)
a5 = a1.intersection(a2)
print(a5)
print(len(a5))
a6 = a2 & a1
print(a6)
#a7= a2-a1 or
a7 = a1.difference(a2) #Removes common elements  from both sets and returns elements from first
print(a7)
a8 = a2-a1
print(a8)

a9 = a1.symmetric_difference(a2) #removes common elements from both sets
#returns all remaining elements
print(a9)
a10 = a2^a1
print(a10)

#intersection_upadate()
a1 = {1,2,3,4}
a2 = {5,1,2,3}
a3 =a1.intersection_update(a2)
print(a3)
print(a1)

#Difference_UPdate(), Symetric_difference_update()
a4 = a1.difference_update(a2)
print(a4)
a5 = a1.symmetric_difference_update(a2)
print(a5)

a1 = {1,2,3,4}
a2 = {5,1,2,3}

print(a1,a2)
a1.add(3)
print(a1,a2)

print(a1.issuperset(a2))
print(a2.issubset(a1))
print(a1.isdisjoint(a2))#it will returns the true when both sets have null intersection


#Dictionaries : A Dictionary is a collection of key,value pairs ,we use
#{K:V} as syntax, keys must be unique , Mutable ,Ordered,indexed through the  keys
#keys can be strings ,numbers (int,float)
data = {1:"balu",2:"deepak",3:"nikhil"}
print(type(data))
print(data)
print(data[1])
print(type(data[2]))

#Dictonaries are mutable collections
details = {'ids': ["CGVI0242","CGVI0249","CGVI0224","CGVI0240"],
                "names":["nikitha","deepthi","vinay","tej"],
                "batch":"pfs-vsp-007",
                 "place":("vizag","vjwd","hyd","bnglre"),
           "subjects":{"python","aptitude","softskills"}}
#print(details)
#print(len(details))
print(details.keys())
print(details["ids"])
print(type(details["ids"]))
details["ids"].append("CGVI0241")
print(details["ids"])
details["ids"].insert(3,"CGVI0235")
print(details["ids"])
print(details["ids"][:3]) #returns the first three ids
print(details["ids"][::2])
'''
#Task : 1)Insert raju at the end also sanju and nihanth at the end in names
             #2)Update subjects with SQL,FLASK,FASTAPI
             #3)remove Bnglre and vizag from place
             #4)Convert batch number to lower case
details = {'ids': ["CGVI0242","CGVI0249","CGVI0224","CGVI0240"],
                "names":["nikitha","deepthi","vinay","tej"],
                "batch":"pfs-vsp-007",
                 "place":("vizag","vjwd","hyd","bnglre"),
           "subjects":{"python","aptitude","softskills"}}


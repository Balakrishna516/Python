#DAY-9 part 2
#COPY(), sort() , reverse()
'''
details = [['sanjay','python',50],['akash','flask',45],['balu','aptitude',30]]
#print(details)
#print(len(details))
#print(type(details))

#copy() -->creates a shallow copy of the given collection
data =details.copy()
#print(data)
#print(len(data))

data[0].append("a")
data.append("vizag")
#details.append("rock")
#data[1].append("bmw")
#data[2].append("gta")
#data.append("ekp")

details.extend(["pfs","jfs"])
print(data)
print(len(data))
print(details)
print(len(details))

#in the below case we have created basic lists so original is not effected
subjects = ['python','mysql','aptitude','softskills']
data = subjects.copy()
#print(data)

#data.insert(2,"frontend")
#print(data)
#print(subjects)
#print(data)

data = subjects
data.insert(2,"frontend")
print(data)
print(subjects)
subjects.remove("python")
data.remove("mysql")
print(data)
print(subjects)

#Sort() , Reverse()
marks = [12,15,20,24,21]
#marks.sort()
#print(marks.sort()) ---> returns none as nothing to be returned
#print(marks)

marks.sort(reverse=True) #it will returns in descending order
print(marks)

marks.append("balu")
#marks.sort() #it will raise TypeError

marks = [12,15,20,24,21]
marks.extend([-23,12,87])
print(marks)
marks.sort(reverse=True)
print(marks)

marks = [12,15,20,24,21]
#print(marks)
marks.extend(["balu",17])
print(marks)
marks.reverse() #this will changes in orginal list
print(marks)
print(marks[::-1])#this will just return the reverse order as 0/p

#min() , max() , len() , type() , sorted()
marks = [20,12,23,25,30]
print(min(marks))
print(max(marks))
a = sorted(marks) # sorted built in function returns a new list with elements in ascending order
print(a)
print(marks)
'''
#Tuples ---> Tuplse are immutiable,Ordered, Indexed collection , it can also have
#duplictaes, we use () to store the data...
'''
data =( )
print(len(data))
print(type(data))

data =1,23,3  # by default it will stores in tuples
print(type(data))
print(data)

data=[] #here it will give zero as o/p because we are not giving any values 
print(len(data))
data=[' '] #here it will give 1 as O/p because we are giving empty string
print(len(data))

data=(' ',)
print(len(data))

#be very specific when we are paSSING DATA uysing ()
#Tuples are Immutable we can not modify the elements in it
#data [-2] = "codegnan" its is not possible
#Nested Tuples (also will have list in it)

details = ("vizag",8,("pfs","jfs","da"),["aptitude","softskills"])
#print(details[2][1]) #Sub INdexing
#print(len(details))
#print(details[2][::2])
print(details[-1])
details[-1].extend(['python','mysql'])
print(details)

#WE CAN NOT MAKE ANY CHANGES OVER TUPLES DIRECTLY BUT WE CAN CHANGE ON LIST
print(details[0].upper())
print(details)

#INDEXING , SLICING , REPETITION, MERGING ARE POSSSIBLE

temp = (23.5,24,24.5)
b=(temp*2)
print(b)
print(temp+b)
print(c)

#Tuples Methods ---> index(),count()
data = (12,3,4,3,45,17)
print(data)
print(data.index(3))
print(data.index(3,2))
print(data.count(3))
b= sorted(data) #returns sorted elements in a  list
print(tuple(b))
c= tuple(sorted(data,reverse=True)) # returns the tuple in descending order
print(c)

del data #it completely eliminates the variables
#print(data) #NameError
'''
#SETS :  A Set is an Unordered, Unique , MUTABLE collection
#Duplictaes

ids =set()
print(ids)
print(type(ids))

names ={"balu","pandu",23,25,23,"pandu"}
print(names)
print(len(names))

#d={1,2,3,4,[1,2,3],5} # we cannot have lists inside a set
#print(d)

d = {12,3,4,(12,3,4),45} #we can have tuples in a set
print(d)

#Task : Create a Nested Tup
le with lists inside it and make all methods
#of lists in the Tuple.

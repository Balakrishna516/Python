'''
sequences --->Strings ,Lists,Tuples,Sets,Forzensets,Dicts

Strings ---> A String is a group of characters,It is immutable,ordered,Indexed Collection.
                   we can denote it is single,double or triple quotes..

data=' '#empty string
print(type(data))
print(len(data))

#operations --> Concatenation,Repatition,Indexed,Slicing
sub1="python"
sub2="Mysql"
print(f"{sub1},{sub2}")#output should be python,Mysql
#python <-> Mysql
print(sub1+" <-> " +sub2)


#repetition --->String can be repeated any number of items with a valid  intation
print("*")
print('*'* 10)
name="balu"
print(f"{name*10}@")
print(f'-------------->{name}')

#Membership ----> in,not in
print("lu"in "Balu")#returns true
print("LU" in "balu")#returns false

#Indexing --->Accesing each position (index) in an object
#it starts with at 0 and ends at len(obj) -1
name="balakrishna"
print(name)
print(len(name))

 #Traversing the elements -->positive Indexing
print(name[1])
#print(name[21])

#Negative Indexing --> starts from back it is denoted as -1 to len(obj)
print(name[-1])
print(name[-4])
#print(name[-16]) #indexed error

a="balakrishna"

#Slicing ---> group of characters ---> [start:End] start is included,end is exclude (len (obj) -1)
print(a[0:7])# here 0 to 7 are included
print(a[7:21])#here 7 to 21 are excluded because 
print(a[0:])
print(a[:])#returns all characters
print(a[:4])
print(a[21:])#it will returns an empty
print(a[5:1])#it will returns empty string as positive slicing lower index to higher index
#name[2]="balu" #strings are immutable

#negative slicing--->
name="balakrishna"
print(name[-1:])#retuns only last character
print(name[-4:-1])
print(name[:-6])#returns balak
print(name[-1:-5])#here it will return an empty string

#Task  --> create a string and explore above possibilities

#Striding--->[start:end:step]  -----> now we can specically get desired characters in an intervals
name="balakrishna"
print(name[::2])#skips alternate element from begining
print(name[::4])
print(name[::1])#it will returns all the elements
name="balakrishna"

place="visakhapatnam"
print(place[:4])
print(place[6:])
print(place[-6:])
print(place[1:7:3])
print(place[-7:-5])
print(place[-7::3])
'''
#what if  we give  -1 in interval
name="balakrishna"
print(name[::-1])#this helps to return in reverse order
print(name[::-2])#this skips one element in reverese order
#you can explore all cases in striding
print(name[1:9:-2]) #it will returns empty 
print(name[-9:-1:1])

#Built----> in functions ---->type(),len(),min(),ord(),chr(),sorted()
name="balu"
print(name)
print(type(name))
print(ord("a"))



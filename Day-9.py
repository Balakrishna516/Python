'''
sequences -> Strings,lists[] ,Tuples() ,Sets set(), Dictionaries {}
Lists [] --> A list is an Ordered,Mutable,Indexed and heterogeneous Collection
it will be dynamic in size

#creation of Lists
details =[12,"balu",8,"pfs",75.7]
print(type(details))
print(len(details))
print(details)


#Nested Lists
batches =[["PFS","PFS-VSP-007","PFS-VSP-008"],
                 ["DA","DA-VSP-007","DA-VSP-008"],
                 "vizag",5]
#print(len(batches))
#print(type(batches))

#Indexing, Slicing, Striding
print(batches[0])
print(batches[-3])
print(batches[1:4])#Observe the output
print(batches[:3])
print(batches[1:4:2])
print(batches[-1])

batches =[["PFS","PFS-VSP-007","PFS-VSP-008"],
                 ["DA","DA-VSP-007","DA-VSP-008"],
                 "vizag",5]
print(batches[-3:-1:2])
print(batches[-1:-5])#observe the output

#sub indexing 
batches =[["PFS","PFS-VSP-007","PFS-VSP-008"],
                 ["DA","DA-VSP-007","DA-VSP-008"],
                 "vizag",5]
print(batches[0])
print(batches[0][1])
print(type(batches[0][1]))
print(batches[0][1][4:7])
print(batches[0][1][4:7][::2])

#lists supports Repetition ,Merging and its also an iterable (iterate  through the Loops)
batches =[["PFS","PFS-VSP-007","PFS-VSP-008"],
                 ["DA","DA-VSP-007","DA-VSP-008"],
                 "vizag",5]
print(batches[0][1])
print(len(batches))
print(batches[0][1][4:11:])
print(batches[1][2])
print(batches[1][2][7:])
print([1,2,3]*3) #repetition
#print([1,2,3]+3)#TypeError
print([1,2,3]+ batches) #Merging

batches =[["PFS","PFS-VSP-007","PFS-VSP-008"],
                 ["DA","DA-VSP-007","DA-VSP-008"],
                 "vizag",5]
print(batches)
print('vizag' in batches) #membership
print('PFS' in batches)
print('PFS' in batches[0]) #returns True
print("DA" in batches[1])
'''

#Lists Methods
'''
data = []
print(dir(data))#returns lists of all available methods
#Append() , Extend() , Insert()
#Append(obj) ---> Insert object to the end of the list
data.append(23)
print(data)
data.append("vizag")
print(data)
#data.append("balu","ba")
print(data)
data.append(["balu","ba"])
print(data)
print(len(data))

marks = [12,13]
print(marks)
marks.append(14)
print(marks)
print(len(marks))
print(type(marks))

#extend() ---> insert multiple elements (objects) to the end of the list
data =[1,2]
data.extend(['python','mysql'])
print(data) #in this case list length becomes 4 as we have inserted
data.extend('vizag') #it will results like 'v' ,'i' ,'z', 'a','z'
print(data)

#Insert(index,object) -->Inserts elements before index
data.insert(2,"balu")
print(data)
data.insert(4,"EKP")
print(data)
data.insert(-1,"b")
print(data)
print(len(data))
data.insert(8,("ball","ant"))
print(data)

marks = [1,2,3,4,5,6,7]
print(marks)
marks[-1]=8
print(marks)
marks[:2]=["balu"]
print(marks)
#IN the above cases data is being modified in original list
#Indexing case length remains constant but data is modified, where as in slicing case it may increase ,decrease

#POP() ,REMOVE() ,CLEAR() --->REMOVES ELEMENTS FROM THE LIST
subjects = ['python','aptitude','ss','mysql','flask']
#pop()----> removes by default last element if index is not mentioned
print(subjects.pop()) #removes and returns last element
print(subjects.pop(2))
#print(subjects.pop(5)) raises error
print(subjects)

#Remove() --->removes specific value from the collection
subjects.remove("python")
#print (subjects.remove("python")) #returns none
print(subjects)
#subjects.remove("codegnan") #VALUE error

#CLEAR() ---> removes all elements from the list and returns empty list
subjects.clear()
print(subjects)

#index(),Count()
#index (start) #returns only first occurance index postion
marks =[24,25,24,26 ,27,30]
print(marks.index(24))
print(marks.index(24,1)) #here we are exclusively giving start position
#print(marks.index(45))#Value Error

#Count() --->returns the count of occurances
print(marks.count(24))
print(marks.count(234))
'''

#Task: Create a Nested lists and Strings and performs List methods
# Nested List Example
students = [
    ["Rahul", 85],
    ["Priya", 92],
    ["Nikhil", 78]
]

print(type(students))
print(students)

# Accessing Nested List Elements
print("First Student Name:", students[0][0])
print("Second Student Marks:", students[1][1])

# Adding a new student (append)
students.append(["Sneha", 88])
print(students)

# Inserting a student
students.insert(1, ["Kiran", 90])
print(students)

# Removing a student
students.remove(["Nikhil", 78])
print(students)

# Sorting by Marks
students.sort(key=lambda x: x[1])
print(students)

# Length of List
print( len(students))





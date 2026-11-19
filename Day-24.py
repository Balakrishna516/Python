#Pass by reference -->
'''
When mutable objects (Lists,sets,dict) are passed into the function,
change inside the affect the original object...

def update(item):
    """we will assume items as list"""
    item.append("Laptop")
    item.extend(["Laptop","Power Bank","Camera"])
cart=['mobile','watch']
print(update(cart))
print(cart)

#Dictionary Usage:--> Update profile
def update(profile):
    """Use of dictionary"""
    profile['branch']='Vizag'
student={'name':['sanjay','akash']}
pfs_student={'Batches':['PFS-VSP-007','PFS-VSP-006'],
             'Subject':['Python','Mysql','Aptitude']}

update(student)
print(student)
update(pfs_student)
print(pfs_student)

#Passby valeu--->Original data will not change,Immutable objects
#Pass by value-->original data will change,mutable objects


#Built in functions--->Finctions

#Built - In functions --> functions which are pre defined is inbuilt in python
#print(),len(),min(),max(),sorted(),int(),float(),bool(),complex(),str(),list(),tuple(),set(),
#dict(),input(),eval(),help()
#print(dir())
#print(dir(__builtins__))#returns list __builtins__ functions and errors
#print(help(print))
#print(help(len))
#abs(),chr(),ord()
print(abs(-34.56)) #returns the absolute value of a numbers
print(chr(176))
print(ord('@'))# return ascii value
data=[1,2,3,4,54]
print(any(data)) #any()--> compares bool(x) for any valure-->true
print(all(data)) #all()--> Needs all values to be present
#print(all(none))
print(bin(6))# return binary obj


print(help(enumerate))

data=['akash','ajay','sanjay']
c=dict(enumerate(data))
print(c)
d=dict(enumerate(data,1))
print(d)
'''
#zip--> it combines mutiple collections into a single collection

data=['sanjay','Deepak','Nikhil','Balu']
marks=[24,32,45]
f=dict(zip(data,marks)) #zip checks for lenght matching
f=list(zip(data,marks))
print(f)









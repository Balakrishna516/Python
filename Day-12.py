'''
Dictionaries ---> A dictionary is a mutable collection,data is indexed using keys,keys must be unique ,Dictionaries methods
'''
details = {'ids' : ['CGVI0242','CGVI0249','CGVI0224','CGVI0240'],
              'names' : ['Nikitha','Deepthi','Vinay','Tej'],
             'batch':'PFS-VSP-007',
             'Place':('Vizag','Vjwda','Hyd','Bnglre'),
             'Subjects':{'Python','Aptitude','Softskills'}}
#print(len(details))

#Membership
''' print('ids' in details)
print('vinay' in details['names']) #we are accessing Via Keys
print('Python' in details['Subjects'])

#print(details*2) #TypeError

#Dictionary is a mutable Collection
details['marks'] = [25,20,18,20]
print(details)
#in above way we can insert new data into dictionary
'''
#Methods on dictionaries:
#print(dir(details)) 
#print(details.keys())  #returns the Dictinonary keys
#print(details.values()) #return sthe dictionary values

#print(details.items()) #returns the key value pairs from dictinonary

#print(details['ids']) #keyerror ---> as the key is not present

 #print(details.get('ids'))

#print(details.get('id')) #as key is not present it returns none

#Inserting multiple keys into Dictionary
'''
data = {'email_ids' : ['nkt@gmail.com','dpt@gmail.com','vny@gmail.com','tej@gmail.com'],
            'linkedin_ids': ['nkt_123', 'dpt_234', 'vinay345','tej13']}
details.update(data)
print(details.keys())
print(len(details))
'''
#Delete data from the dictionary
#Pop(key) ---> removes specified data from the dict
'''
print(details)
details['marks'] = [25,20,18,20]
print(details)
print(details.pop('email_ids'))
print(details)
print(details.clear())
print(details)
print(details.pop('marks'))
'''
#del details [['marks','ids']] #not possible
#del details ['names'],details['ids'] #to delete multiple pairs at atime
#print(details.keys())

#print(details.keys())

#setdefault() --->inserts key into the dictionary if it is not present
'''
details.setdefault('status')
print(details.keys())
print(details)
details['status'] =['placed','active','onhold']
print(details)

print(details.setdefault('ids')) # asws already have ids in dict
#it just prints the values
print(details.keys())
'''
#fromKeys() --->Create a new dict from iterable
'''
duration = [34,20,34,12]
data = dict.fromkeys(duration) #we get 3 keys only as 34 present in dict
print(data)
data = dict.fromkeys(duration,['flask','sql','fastapi'])
print(data)
data [34] = 'python'
data [20] = 'Mysql'
print(data)

name =dict.fromkeys('Balakrishna')
print(name)
'''
#Nested Dictionaries ---> A dictionary inside another dictionary
'''
students = {'s1' : {'name':'balu',
                     'id':'cgvi0240',
                     'batch':'pfs-vsp-007'},
             's2':{'name':'deepak',
                    'id':'cgvi0241',
                    'batch':'pfs-vsp-008'}}
print(students)
print(len(students))
print(students.keys())
print(type(students['s1'])) #Return the Dict
print(students['s1'].keys())

print(students['s1']['id'])

#for student s1 update subjects,marks
#students['s1'].update({'subjects':['python','java'],'marks':[95,97]})
#print(students['s1'])

students['s1']['subjects'] =['Python','Mysql']
students['s1']['marks']=[20,27]
print(students['s1'])
'''
#Task : Create your student profile with fields as ids number
#Email id,Mobile Number,Parent Whatsappnumber,subjects,
#batch no, daily exam marks,weekly exam marks,batch rank,
#github_url,Linkedin_id

#Frozensets ---> Frozensets are unordered, it also an immutable collection

data =frozenset()
print(data)
print(type(data))
data = frozenset (['balu',23,'vizag'])
print(data)
print(type(data))
print(len(data))
print(data.union(data)) #Within itself but no change


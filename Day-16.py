'''
usage of for with conditional statements

#notifications=[0,0,0,0]
notifications=[1,1,1,1]
#notifications=[1,0,1,0]
#0 ---->Notification read
#1----->unread notification
#Notification Checker
for notification in notifications:
    if notification == 1:
       #U need to map a condition 
        print("unread Notification")
else:
    print("All notifications are caugth up")
#print("All notifications are caught")

#Searching Scenario same above program to be Transformed --->
#notifications=[0,0,0,0]
notifications=[1,1,1,1]
#notifications=[1,0,1,0]
#0 ---->Notification read
#1----->unread notification
#Notification Checker
for notification in notifications:
    if notification == 1:
       #U need to map a condition 
        print("unread Notification")
        break #it exits early,the else block will be skipped
else:
    print("All notifications are caugth up")
#print("All notifications are caught")

#Break: ----> terminate the flow of the program
#searching in a List
#you want to handle the"item not found"case

fruits = ["apple","banana","kiwi","cherries"]
item = input("which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f"you got your desired {item}")
        break
else:
      print(f"could not find {item} in the fruits")
'''
#Continue ---> will skip the current itteration and proceeds for the remaining iteration
'''
fruits = ["apple","banana","kiwi","cherries"]
item = input("which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f"you got your desired {item}")
        continue
else:
      print(f"could not find {item} in the fruits")

notifications =list(map(int,input("enter:").split(",")))
#notifications=[1,1,1,1]
#notifications=[1,0,1,0]
#0 ---->Notification read
#1----->unread notification
#Notification Checker
for notification in notifications:
    if notification == 1:
       #U need to map a condition 
        print("unread Notification")
        continue
else:
    print("All notifications are caugth up")
'''
#While --->loops --> it is mainly used when we rely codition,it will be completely executed until the condition is satisified

'''
while <condition>:
           statement(s)....
           .......
'''
'''
while True:
    print("yes") #it will runs an infinite loop we need to keyboard interrupt

#initalizier with which we need to initalise

i = 0 # initialised statement
while i<10:
    print(i)
    i = i+1 # counter
'''
#get the counter from 10 to 1 using while
'''
i=10
while i>=1:
    print(i)
    i=i-1
'''
i=0
while i<=10:
    print(10-i)
    i = i+1


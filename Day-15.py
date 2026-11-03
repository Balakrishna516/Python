#Range(stop) ---> takes by default minimum values as 0
'''
for i in range(5):
    print(f'value of i is {i}')
    print(f'square of i is {i**2}')
'''
#range(start,stop) --> u can mention start and stop postion(values)
#Start is include,end is excluded
'''
for i in range(1,11):
    print(i,i**2)
    print('####')
'''
#Range(start,stop,step)
'''
for i in range (1,21,1):
    print(i)
for i in range (1,21,2):
    print(i)
'''
#get first 10 even numbers
'''
for i in range(2,21,2):
    print(i)
#print numbers from 10 to 1 in reverse order
for i in range(10,0,-1):
    print(i,end=" ")

#print 'A' to 'Z' in a single line
for i in range (65,91):
    print(chr(i),end=" ")

names =['balu','pandu','pavani','utr','ganga']
for name in names:
    print(name,end=" ") #this returns in horizontal order
    
for i in range (len(names)):
    print(names[i])

#ASK integer input from the user and get the sum of numbers per unit
a=int(input( "enter the value:"))
if a>0:
    total=0
    for i in range(a+1):
        total=total+i
        print(f'total of {i} is {total}')
else:
      print("no output")
'''
#Usecase : Checking daily workout app usage
#1---> workout done
#0 ---> workout missing
#find the longest streak

work_log =[1,1,1,0,1,1,0]
longest_streak=0
current_streak=0
for day in work_log:
    if day ==1: #here we use day to understand the workout days
        current_streak = current_streak+1
        if current_streak > longest_streak:
            longest_streak=current_streak
    else:
        current_streak =0
print(f'Longest streak is {longest_streak}')

'''
usage of for with for....
Nested Loops ---> Loops inside the another loop.they are commonly used in pattern printing,matrix opertaions
and solving various algo.Problems

Syntax:

for i in range(outer_loop_range):
      for j in range(inner_loop_range):
      #code
'''
#understand with the simple Example:
'''
for i in range(3): #Outer loop runs 3 times
    for j in range(2): #Inner loop runs 2 times for each outer loop
        print(f"i ={i},j ={j}")
'''        

#for every outer loop inner loop will be completely executed...
#Outer loop ---> rows --->inner loop --->coloumns
'''
for i in range(2):   #i---->0,1
    for j in range(4): #j ---->0,1,2,3
        print(i,j)
 '''
#NUMBER Patterns --->Row based number patterns,Column based number patterns....
'''
1 2 3
1 2 3
1 2 3

for i in range(1,4): #i---->1,2,3
    for j in range(1,4):#j --->1,2,3
          # print(i,j)
           print(j,end=" ")
    print()
'''
'''
1 1 1 1 1
2 2 2  2 2
3 3 3 3 3
4 4 4 4 4
'''
'''
for i in range(1,5): #i --->1,2,3
    for j in range(1,6):#J--->1,2,3
        #print(i,j)
        print(i,end=" ")
    print()
'''
'''
A A A A A
B B B B B
C C C C C
'''
'''
for i in range(1,4):
    for j in range(1,6):
        print(chr(64+i),end=" ")
    print()

#EX:
#A B C D
#A B C D
#A B C D
for i in range(1,5):
    for j in range(1,5):
        print(chr(64+j),end=" ")
    print()
'''
'''
EX:
1 2 3
4 5 6
7 8 9

num =1
for i in range(1,4):
    for j in range(1,4):
        print(num,end=' ')
        num=num+1
    print()    
'''
#Square Pattern ---> * with n rows and columns
'''
n= int(input("enter the value:"))  
for i in range(n):
    for j in range(n):
        print('*',end=" ")
    print()
    
output:
* * * 
* * * 
* * *
'''
#Change this with different values
'''
n =int(input("enter the value:"))
for i in range(n):
    for j in range(n+1):
        print('@',end=" ")
    print()
output:
@ @ @ @ @ @ 
@ @ @ @ @ @ 
@ @ @ @ @ @ 
@ @ @ @ @ @ 
@ @ @ @ @ @
'''
#Right angled triangle
'''
*
* *
* * *
* * * *
* * * * *

for i in range(1,6):
    for j in range(i):
        print('*',end=' ')
    print()
'''
#Inverted Triangle
'''
* * * * *
* * * *
* * *
* *
*

n=int(input("enter the value:"))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()
'''
'''
#TASK TO DO

1
2 3
4 5 6
7 8 9 10

A
B C
D E F
G H I J

A
A B
A B C
A B C D
A B C D E

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
#TASK ANSWERS
#EX:
'''
for i in range(1,6):
    for j in range(i):
        print(j+1,end=" ")
    print()
'''
#output:
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
#EX:
'''
for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
'''
#output:
'''
A 
A B 
A B C 
A B C D 
A B C D E
'''
#EX:
'''
num =1
for i in range(1,5):
    for j in range(i):
        print(num,end=' ')
        num=num+1
    print()
'''
#OUTPUT:
'''
1
2 3
4 5 6
7 8 9 10
'''
#EX:
'''
num =1
for i in range(1,5):
    for j in range(i):
        print(chr(64+num),end=' ')
        num=num+1
    print()
'''
#OUTPUT:
'''
A
B C
D E F
G H I J
'''





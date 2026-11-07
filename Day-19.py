#STAR PYRAMID PATTERN
'''
                 *
              *     *
          *     *      *
        *    *   *     *
'''
#EX:
'''
n=int(input("enter the value:")) #---->3
for i in range(1,n+1):  #--------------->(1,4)
    for j in range(1,n+1):#----------------->(1,4)
        if j  <= n-i:
           print(" ",end="")
        else:
            print("*",end=" ")
    print()       
'''
#for inverted STAR PYRAMID PATTERN
'''
n=int(input("enter the value:")) 
for i in range(1,n+1):  
    for j in range(1,n+1):
        if j  <= n-i:
           print("*",end=" ")
        else:
            print("",end="")
    print()
'''
#USING FOR LOOP
#upper
'''
n=int(input("enter:"))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
#lower
for i in range(n):
    print(" "*(i+1)+"* "*(n-i-1))
'''
#output:
      * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 

    

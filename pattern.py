print('     *')
for i in range(1,4):
    for j in range(1,5-i):
        print(' ',end='')
    print('*',end='')
    for k in range(1,2*i):
        print(" ",end="")
    print("*")
    for a in range(1,2*i):
        print("*",end="")
    print()
for i in range (4,0,-1):
    for j in range(1,5-i):
         print(' ',end='')
    print('*',end='')
    for k in range(1,2*i):
        print(" ",end="")
    print("*")
print("     *")
        
    

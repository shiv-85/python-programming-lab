x=input("enter the string")
for i in range (0,len(x)):
 if i%2==0:
     print(x[i].upper(),end='')
 else:
     print(x[i].lower(),end='')

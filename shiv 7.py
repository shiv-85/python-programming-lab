a1=list(map(int,input("enter the values").split()))
add=0
odd=0
for i in a1:
    if i%2==0:
        add=add+i
    else:
        odd=odd+i
print("sumof even digit",add)
print("sumof odd digits",odd)

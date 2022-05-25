a=list(map(int,input("enter the list").split()))
x=a[0]
y=a[-1]
a[-1]=x
a[0]=y
print(a)

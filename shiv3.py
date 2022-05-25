a=int(input("enter the number"))
y=a**2
summ=0
while(y>0):
    n=y%10
    summ=summ+n
    y=y//10
if a==summ:
    print("neon hai")
else:
    print("neon nahi hai")

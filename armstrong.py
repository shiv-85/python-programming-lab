a=int(input("enter the number"))
temp=a
sum=0
while(a>0):
    remainder=a%10
    sum=sum+remainder**3
    a=a//10
if(temp==sum):
    print("the number is armstrong")
else:
    print("the number is not armstrong")


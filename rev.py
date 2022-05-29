x=input("enter the string")
a=int (input("enter the number"))
rev=0
while(a>0):
  rem=a%10
  rev=(rev*10)+rem
  a=a//10
print("\n reverse of entered number is = %d"%rev)


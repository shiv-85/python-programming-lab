
a=int (input("enter the number"))
y=a
rev=0
while(a>0):
  rem=a%10
  rev=(rev*10)+rem
  a=a//10
print(" reverse of entered number is ",rev)
if rev==y:
   print("number is palindrome")
else:
   print("not palindrome")

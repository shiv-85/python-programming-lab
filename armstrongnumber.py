"""Program to print natural number from n to 1
n=int(input("Enter the valueof n:-"))
i=n
while i>=1:
    print(i)
    i=i-1"""
"""Write a program to print odd numbers
i=1
n=int(input("Enter the value of n:-"))
while  i<=n:
    print(i)
    i=i+2"""
"""Write a program to print even number from n to 1 and n must be 1
n=int(input("Enter the value of n:-"))
i=n
while  i>=1:
    print(i)
    i=i-2"""
"""Write a program to print the tablr of n
i=1
n=int(input("Enter the value of n:- "))
while (i<=10):
    pro=n*i
    print(pro)
    i=i+1"""
"""Write a program to print the sum of digits
n=int(input("Enter the value of n:-"))
suma=0
while (n!=0):
    last_digit = n%10
    suma=suma + last_digit
    n=n//10
print("The sum of digits = ",suma)"""
"""Write a program to print reverse the number
n=int(input("Enter the valueof n:-"))
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reversed number = ",rev)"""
"""Write a program to check whether it is pallindrome or not
n=int(input("Enter the value of n:-"))
rev=0
num=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(rev==num):
    print("The number is pallindrome")
else:
    print("The number is not pallindrome")"""
"""Write a program to check whether the number is armstrong or not
n=int(input("Enter the value of n:-"))
num=n
nu=0
sum=0
while n!=0:
    n=n//10
    nu=nu+1
n=num
while n!=0:
    l=n%10
    ls=l**nu
    n=n//10
    sum=sum+ls
if(num==sum):
    print("The number is armstrong")
else:
    print("The number is not armstrong")"""
"""Write a program to find the armstrong number from 1 to n """
nt=int(input("Enter the value of n:-"))
i=100
while i<=nt:
    n=i
    num=n
    nu=0
    sum=0
    while n!=0:
        n=n//10
        nu=nu+1
    n=num
    while n!=0:
            l=n%10
            ls=l**nu
            n=n//10
            sum=sum+ls
    if(sum==num):
        print(num)
    i=i+1
   

    




    

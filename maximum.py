a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
z=lambda a,b:a if a>b else b
print("The max no. is",z(a,b))

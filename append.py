n=int(input("Enter the list"))
size=[]

for i in range(0,n):
    element=input()
    size.append(element)

print("maximum in list is",max(size))

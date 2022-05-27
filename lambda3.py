n=int(input("Enter the no.of string"))
lis=[]
for i in range(n):
    lis.append(input())
print(list(map(lambda x:len(x),lis)))

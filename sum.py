
S1={1,2,3}
S2={3,4,5}
print(S1.union(S2))
print(S1.intersection(S2))
print(S1&S2)
print(S1.difference(S2))
print(S2-S1)
print(S1.symmetric_difference(S2))
print(S1^S2)


s1={1,2,3,4,5,6,13,45,64}
print(s1)

s1='hello i am in gla'
for i in set(s1):
    k=s1.count(i)
    print(i,'is occuring',k,'times')

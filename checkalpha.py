d={}
for i in range(97,123):
    a=(chr(i))
    b=i
    d[a]=b
    
print(d)
s=0
d1={}


a="g"
b="u"
c="p"
d="t"
e="a"
f=ord("g")
g=ord("u")
h=ord("p")
i=ord("t")
j=ord("a")
d1[a]=f
d1[b]=g
d1[c]=h
d1[d]=i
d1[e]=j
print(d1)
for i in d1.values():
    s=s+i
print(s)

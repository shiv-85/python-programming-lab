#10
'''
def isAnagram(s1,s2):
    #s1=input("enter a str1:- ")
    #s2=input("enter the str2:- ")
    x=s1.upper()
    y=s2.upper()
    if len(s1)==len(s2):
        sorts1=sorted(x)
        sorts2=sorted(y)
        if sorts1==sorts2:
            return("both are anagram")
        else:
            return("not anagram")
    else:
         return("not anagram")
         
    
s1=input("enter a str1:- ")
s2=input("enter the str2:- ")    

print(isAnagram(s1,s2))
#11

import string

def panagrams(s):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in str.lower(s):
            return False
    
    return True
s=input("enter a string of your choice:- ")
if (panagrams(s)==True):
    print("YES")
else:
    print("no")
'''
#8
def myTitle(s):
    l=s.split()
    l2=[]
    for i in l:
        s1=''
        p=''
        if ord(i[0])>=97 and ord(i[0])<=122:       #phele word ke phelel letter ka
            p=chr(ord(i[0])-32)
        else:
            p=i[0]
        for j in i[1:]:
            if ord(j)>=65 and ord(j)<=90:    #
                s1=s1+chr(ord(j)+32)
            else:
                s1=s1+j
        l2.append(p+s1)
    print(' '.join(l2))
myTitle(input("enter the str:- "))
    

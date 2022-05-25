def toupper(s):
    r=''
    for i in s:
        if ord(i)>=97 and ord(i)<=122:
            r=r+chr(ord(i)-32)
        else:
            r=r+i
    print(r)
            
toupper(input())

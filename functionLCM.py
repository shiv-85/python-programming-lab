def myLCM(a,b):
    larger=max(a,b)
    for i in range(larger,a*b+1):
        if i%a==0 and i%b==0:
            print("LCM is ",i)
            break
myLCM(int(input()),int(input()))
    

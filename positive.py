n=int(input("enter a number"))
try:
    if n>0:
        print ("positive")
    else:
        raise ValueError
except ValueError:
    print("negative")

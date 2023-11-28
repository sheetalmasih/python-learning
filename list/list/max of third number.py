a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b:
    max=a
    min=b
else:
    max=b
    min=a
if c>a:
    max1=c
    min1=a
else:
    max1=a
    min1=c
if min>min1:
    if min>max1:
        print("third max",max1)
    else:
        print("third max",min)
else:
    if min1>max:
        print("third max",max)
    else:
        print("third max",min1)
    
l=[5,8,9,12,15,17]
key=int(input())
size=len(l)
mid=0
i=0
j=size-1
flag=0
while flag==0:
    mid=(i+j)//2
    if l[0]==key:
        mid=i
        flag=1
        break
    elif l[-1]==key:
        mid=size-1
        flag=1
        break
    elif l[mid]==key:
        flag=1
        break
    elif l[mid]>key:
        j=mid
    elif l[mid]<key:
        i=mid
if flag==1:
    p=l.index(l[mid])
    print("number is found",l[mid],p)
else:
    print("number is not found")

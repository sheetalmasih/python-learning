# n=int(input("enter a number:"))
# list=[4,6,7,8,12,34,67,88,96,108,398]
# l=0
# u=len(list)-1
# while l<=u:
#     mid=(l+u)//2
#     if list[mid]==n:
#         print(True)
#     else:
#         if list[mid]<=n:
#             l=mid
#         else:
#             u=mid
# if list[mid]==n:
#     print("found at",list[mid])
# else:
#     print("not found")

#########################################
a=[]
size=int(input("enter a number:"))
for i in range(size):
    val=int(input())
    a.append(val)
key=int(input("enter a number:"))
i=0
j=size-1
flag=0
while i<=j and flag==0:
    mid=(i+j)//2
    if a[mid]==key:
        flag=1
        pos=mid+1
    if a[mid]>key:
        j=mid-1
    if a[mid]<key:
        i=mid+1
if flag==1:
    print("number found at",pos)
else:
    print("not found")

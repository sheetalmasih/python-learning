# a=[]
# for i in range(3):
#     b=[]
#     for j in range(3):
#         val=int(input("enter a number:"))
#         b.append(val)
#     a.append(b)
# for i in range(3):
#     for j in range(3):
#         print(a[i][j],end="  ")
#     print()
# sum1=0
# sum2=0
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             sum1+=a[i][j]
#         if i+j==3-1:
#             sum2+=a[i][j]
# if sum1!=sum2:
#     f=1
# else:
#     for i in range(3):
#         sumr=0
#         sumc=0
#         for j in range(3):
#             sumr+=a[i][j]
#             sumc+=a[j][i]
#         if sumr!=sum1:
#             f=1
#         elif sumc!=sum1:
#             f=1
#         else:
#             f=0
# if f==0:
#     print("matrix is magic square")
# else:
#     print("martix not magic sqare")
            

a=[]
for i in range(3):
    b=[]
    for j in range(3):
        val=int(input())
        b.append(val)
    a.append(b)
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()
sum1=0
sum2=0
for  i in range(3): 
    for j in range(3):
        if i==j:
            sum1+=a[i][j]
        if i+j==3-1:
            sum2+=a[i][j]
if sum1!=sum2:
    f=1
else:
    for i in range(3):
        sumr=0
        sumc=0
        for j in range(3):
            sumr+=a[i][j]
            sumc+=a[j][i]
        if sumr!=sum1:
            f=1
        if sumc!=sum1:
            f=1
        else:
            f=0
if f==0:
    print("metrix is megic square ")
else:
    print("metrix is  not megic square")
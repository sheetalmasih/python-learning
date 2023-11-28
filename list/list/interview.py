# str=input("enter a sentence : ")
# upper=0
# lower=0
# i=0
# while i<len(str):
#     j=0
#     while j<len(str[i]):
#         if str[i][j]>='a' and str[i][j]<='z':
#             lower+=1
#         elif str[i][j]>='A' and str[i][j]<='Z':
#             upper+=1
#         j+=1
#     i+=1
# print("upper : ",upper)
# print("lower : ",lower)

# x=[1,2,3,3,3,4,4,5,6,7]
# i=0
# while i<len(x):
#     if x[i]==4:
#         print(i)
#         #break
#     # else:
#     #     pass
#     i+=1

x=[1,2,4,3,5,7]
m=[]
for i in range (len(x)):
    n=[]
    o=[]
    if x[i]%2==0:
        n.append(x[i])
    else:
        o.append(x[i])
m.append(n)
m.append(o)
print(m)
    
    
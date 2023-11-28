# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1,):
#         print(j,end=" ")
#     print()
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
##########################################3
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     for j in range(0,2*n-2*i):
#         print(" ",end='')
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

###################################################
# rows = int(input("Enter Rows = "))
# i = 1
# while(i <= rows):
#     j = 1
#     while(j <= i):
#         print(j, end = '')
#         j = j + 1
#     k = 1
#     while(k <= 2 * (rows - i)):
#         print(end = ' ')
#         k = k + 1
#     l = i
#     while(l >= 1):
#         print(l, end = '')
#         l = l - 1
#     print()
#     i = i + 1
################################################
# rows = int(input("Enter V Number Pattern Rows = "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end = '')
#     for k in range(1, 2 * (rows - i) + 1):
#         print(end = ' ')
#     for l in range(i, 0, -1):
#         print(l, end = '')
#     print()
#################################################
# t=int(input("enter no of test cases "))
# for i in range(t):
#     c=int(input("enter any no between 1 to 6 "))
#     a=int(input("enter value "))
#     if c<=6:
#         b=int(input("EMTER  value "))
#         if c==1:
#             print(a+b)
#             print(a+b)
#         elif c==2:
#             print(a-b)
#         elif c==3:
#             print(a*b)
#         elif c==4:
#             print(a//b)
#         elif c==5:
#             print(a%b)
#         elif c==6:
#             print("exit")
#     else:print("Invalid")
#########################################################
# t=int(input("t"))
# for i in range(t):
#     n=int(input("n"))
#     l=list(map(int,input().split()))
#     x=int(input())
#     count=0
#     l.sort()
#     for k in range(1,n-2):
#         i=k+1
#         j=n-1
#         while (i<j):
#             if l[k]+l[i]+l[j]==x:
#                 count=1
#                 break
#             elif l[k]+l[i]+l[j]<x:
#                 i+=1
#             else:
#                 j-=1
#                 count+=1
#     print(count)
#############################################
# t=int(input("t"))
# for i in range(t):
#     n=int(input("n"))
#     l=list(map(int,input().split()))
#     x=int(input())
#     count1=0
#     for i in range(n-2):
#         j=i+1
#         k=n-1
#         while(j<k):
#             if l[i]+l[j]+l[k]<x:
#                 count1+=(k-j)
#                 j+=1
#             else:
#                 k-=1
#     print(count1)
    #####################################################
    
# t=int(input())
# for i in range(t):
#     n=int(input("enter a n number:"))
#     l=list(map(int,input().split()))
#     x=int(input("enter a number:"))
#     count=0
#     for k in range(1,n):
#         i=k
#         j=n
#         while i<j:
#             sum=l[k]+l[i]+l[j]
#             if sum==x:
#                 print(count)
#                 i+=1
#             elif sum!=x:
#                 count+=1
#             else:
#                 j-=1
                
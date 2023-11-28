                     #list  assignment#    
# question number==1:
# house_list=[]
# for i in range(4):
#   a=input()
#   house_list=house_list+[a]
# print("house list = ",house_list)
#..................................................................
# question number==2:
list=["Mercury","Venus","Earth","Mars","Jupiter","Saturn", "Uranus","Neptune"]
b=int(input("enter a number:"))
for i in range(len(list)):
  if i==b:
    print(list[i])
#.........................................................................
# question number==3:
# a=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# for i in range(len(a)):
#   if i%2!=0:
#     print(a[i], end=" ")
#...........................................................................
# question number==4:
# # a=[]
#  i=0
#  while i<20:
#    if i%2==0:
#      a.append(i)
#    i+=1
#  print(a)
#...............................................................................
# question number==5:
#list=[]
# for i in range(4):
#    a=int(input("enter a number:"))
#    list.append(a)
#   print(list)
#.................................................................................
# question number==6:
# a=[]
# list=int(input())
# for i in range(list):
#   val=int(input())
#   a=a+[val]
# b=int(input())
# if b in a:
#   print("yes")
# else:
#   print("no")
#.......................................................................
# question number==7:
# a=[]
# list=int(input("enter a nu:"))
# for i in range(list):
#   val=int(input("enter ele:"))
#   a=a+[val]
# print(a)
# for j in range(len(a)):
#   if a[i]>a[j]:
#     print(a[j])
#........................................................................
# question number==8:
# a=[]
# list=int(input(""))
# for i in range(list):
#   val=int(input(""))
#   a=a+[val]
# print(a)
# b=int(input())
# print(a.count(b))
#....................................................................
#  question number===9:
# list=['T', 'H', 'T', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'H', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'H', 'T', 'H', 'T', 'H'] 
# count=0
# count_h=0
# count_t=0
# i=0
# while i<len(list)-1:
#   if list[i]=="H":
#     count_h+=1
#     count_t=0
#   if list[i]=="T":
#     count_t+=1
#     count_h=0
#   if count_h>=3 and list[i+1]=="T" or count_t>=3 and list[i+1]=="H":
#     count+=1
#   i+=1
# print(count)
# # #..................................................................
# question number==10:
# a=[]
# for i in range(4):
#   b=[]
#   for j in range(4):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
#................................................................
# question number===11:
# arr=int(input("enter a number:"))
# a=[]
# for i in range(arr):
#   b=[]
#   for j in range(arr):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
#.........................................................................
# question number===12:
# arr=int(input("enter a number:"))
# a=[]
# for i in range(arr):
#   b=[]
#   for j in range(arr):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
#...............................................................................
# question number==13:
#arr=int(input("enter a number:"))
#a=[]
#for i in range(arr):
#   b=[]
#   for j in range(arr):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
# for i in range(4):
#     print(a[i][2]) # third coloumn
# print(a[1][0:4])  # second row
#................................................................................
#..................................................................
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#   for j in i:
#     print([j][1])
#....................................................................
# question number==14:
# m=int(input("enter a number:"))
# n=int(input("enter a number"))
# a=[]
# for i in range(m):
#   b=[]
#   for j in range(n):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
#.....................................................................
# question number==15:
# arr=int(input("enter a number:"))
# a=[]
# for i in range(arr):
#   b=[]
#   for j in range(arr):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
# print(a[1][0:4])  # second row

#.......................................................................
# question number==16:
# n=int(input("enter a nuber:")) 
# a=[]
# for i in range(n):
#   b=[]
#   for j in range(4):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
# print(a[2][0:4])  # third row
#...........................................................................
# question number==17:
# n=int(input("enter "))
# a=[]
# for i in range(n):
#   b=[]
#   for j in range(4):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
# print(a[2][0:4])  # nth row
#..............................................................................
# question number==18:
# m=int(input("enter "))
# a=[]
# for i in range(m):
#   b=[]
#   for j in range(4):
#     list=int(input())
#     b.append(list)
#   a.append(b)
# print(a)
# print(a[2][0:4])  # mth row
#...............................................................................
# question number==19:
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# for i in range(6):
#     for j in range(9):
#         if j<8:
#             print(grid[j][i],end=" ")
#         else:
#             print(grid[j][i])
#...................................................................................
                       #withouht using append function: 
# n=int(input(""))
# a=[0]*n
# i=0
# while i<n:
#     b=int(input(""))
#     a[i]=b
#     i+=1
# print(a)

#.........................................................................................
# question number==20:
# num=int(input("enter a number:"))
# list=[[0 for x in range(num)] for y in range (num)]
# n=1
# low=0
# high=num-1
# count=int((num+1)/2)
# for i in range(count):
#     for j in range(low,high+1):
#        list[i][j]=n
#        n+=1
#     for j in range(low+1,high+1):
#      list[j][high]=n
#      n+=1
#     for j in range(high-1,low-1,-1):
#      list[high][j]=n
#      n+=1
#     for j in range(high-1,low,-1):
#       list[j][low]=n
#       n+=1
#     low+=1
#     high-=1
# for i in range(num):
#   for j in range(num):
#     print(list[i][j],end="  ")
#   print()
            
        
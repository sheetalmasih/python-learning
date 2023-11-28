# s='Welcome to My Site https://nayaksworld.com '
# print(s.find('come'))
# print(s.find('o'))
# print(s.find('o', 10, 20))
# print(s.find('o', 5, 10))

#############################################
# s='My' 
# s1='Blog'
# s2=s[:1]+s1[len(s1)-1:]
# print(s2)

#################################
# print(6 + 3)
# print('6' + '3')
# print('a' + 'b' + 'c')
##########################################################

# date=input("Enter the date: ")
# d,m,y=date.split('/')
# d=int(d)
# m=int(m)
# y=int(y)
# if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
#     max1=31
# elif(m==4 or m==6 or m==9 or m==11):
#     max1=30
# elif(y%4==0 and y%100!=0 or y%400==0):
#     max1=29
# else:
#     max1=28
# if(m<1 or m>12):
#     print("Date is invalid.")
# elif(d<1 or d>max1):
#     print("Date is invalid.")
# elif(d==max1 and m!=12):
#     d=1
#     m=m+1
#     print("The incremented date is: ",d,m,y)
# elif(d==31 and m==12):
#     d=1
#     m=1
#     y=y+1
#     print("The incremented date is: ",d,m,y)
# else:
#     d=d+1
#     print("The incremented date is: ",d,m,y)

############################################################

# l=[1,5,3,5,5,6,7]
# choose=int(input())
# count=0
# for i in l:
#     if i==choose:
#         count+=1
# print(count)

############################################################

#number automorphic or not :
 
# num=int(input())  
# square=num*num    
# flag=0   
# while(num>0):   
#     if(num%10!=square%10):  
#         print("No, it is not an automorphic number.")  
#         flag=1  
#         break                       
#     num=num//10                        
#     square=square//10   
      
# if(flag==0):  
#     print("Yes, it is an automorphic number.")  

########################################################
# count sum pairs:
# arr = [1, 5, 7, -1, 5]
# n = len(arr)
# sum = 6
# count = 0 
# for i in range(0, n):
#     for j in range(i + 1, n):
#         if arr[i] + arr[j] == sum:
#             count += 1
# print(count)

#############################################################
# third max of four number:
# n=int(input("enter a number:"))
# i=1
# while i<=n:
#   a=int(input("enter a nmber:"))
#   if i==1:
#     max=a
#     smax=max
#     tmax=max
#   elif a>max:
#     tmax=smax
#     smax=max
#     max=a
#   elif a>smax:
#     tmax=smax
#     smax=a
#   elif a>tmax:
#     tmax=a
#   i+=1
# print(tmax)

#################################################################
# sec max of thre numbers:

# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:
#     if a<c:
#         print(a)
#     elif b>c:
#         print(b)
#     else:
#         print(c)
# elif a<b:
#     if a>c:
#         print(a)
#     elif b<c:
#         print(b)
#     else:
#         print(c)

#########################################################
# n=int(input())
# if n%5==0 and n%8==0:
#     print("Hello")
# else:
#     print("Bye")

###########################################################
#  15 Check if the user number has a middle number or not. If it has then you
# have to print “odd winner” otherwise “even winner”.
# n=[1,2,3,3,5,3,7,6,7,8]
# print(n[int(len(n)//2)])
# if len(n)%2==0:
#     print("even winner")
# else:
#     print("odd winner")

#######################################################
# if a>b and c<=d

#######################################################
# n=int(input())
# min=9
# while n>0:
#     digit=n%10
#     if min>digit:
#         min=digit
#     n=n//10
# print(min)

#######################################################

t=int(input("enter the temperature : "))
x=input("enter c/f:")
f=(t*1.8)+32
c=(t-32)*5//9
if x=="c":
  if c>=35:
    print(f, "fernehiet,very hot")
  elif c>=30 and c<=35:
    print(f,"hot")
  elif c>=20 and c<=25:
    print(f,"fernehiet, cold")
  elif c<=19:
    print(f," fernehiet,very cold")
  elif c>=26 and c<=29:
    print(f,"fernehiet,normal")
elif x=="f":
  if f>=43 and f<=51:
    print(c,"celsius,cool")
  elif f<=14:
    print(c,"celsius,very cold")
  elif f>=14 and f<=42:
    print(c,"celsius,cold")
  elif f>=52 and f<=71:
    print(c,"celsius,normal")
  elif f>=72 and f<=89:
    print(c,"celsius,warm")
  elif f>=90:
    print(c,"celsius,hot")


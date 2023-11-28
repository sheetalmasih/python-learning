# n=int(input("enter a number:"))
# i=1
# count=0
# while i*i<=n:
#     if n%i==0:
#         print(1,n//i)
#         count+=1
#     i+=1
# if count==1:
#     print("prime no")
# else:
#     print("not prime")

# a=[]
# list=int(input())
# for i in range(list):
#   val=int(input())
#   a=a+[val]
# print(a)
# b=int(input())
# if b in a:
#   print("yes")
# else:
#   print("no")

# a=[]
# list=int(input("enter a nu:"))
# for i in range(list):
#   val=int(input("enter ele:"))
#   a=a+[val]
# print(a)
# for j in range(len(a)):
#   if a[i]>a[j]:
#     print(a[j])
# i=100
# while i<=999:
#   s=0
#   n=i
#   while n>0:
#     digit=n%10
#     s+=digit**3
#     n=n//10
#   if s==i:
#     print(i)
#   i+=1
i=2
while i<10000:
  j=2
  s=1
  while j*j<=i:
    if i%j==0:
      s+=j
      if j!=i//j:
        s=s+i//j
      j+=1
if s==i:
  print(i)
i+=1
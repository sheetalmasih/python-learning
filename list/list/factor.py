from re import I


# n=int(input("enter a number:"))
# i=0
# count=0
# while count<=n:
#     n=n*i
#     print(n)
#     n-=1
#     count+=1
# print(count)
    
    
    
# i=232792560
# c=0
# while i>=i:
#   j=1
#   while j<=20:
#     if j%i==0:
#        c+=1
#     j+=1
#   if c==20:
#      print(i)
#   i+=1


# flag=0
# i=2520
# while i>0:
#   for j in range(11,21):
#     if i%j==0:
#       flag+=1
#   if flag==10:
#     print(i)
#     break
#   flag=0
#   i+=20


div = 10001
i = 2
count = 0
prime = 0
now = []
while count < div:
    for x in range (2,i+1):
        if len(now) ==2:
            break
        elif i%x == 0:
            now.append(x)
    if len(now)==1:
        prime = i
        count += 1
    now = []
    i+=1       
print(prime)
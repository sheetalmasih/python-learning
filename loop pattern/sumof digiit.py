a=int(input("enter a number:"))
digit=0
sum=0
while a>0:
    digit=a%10
    sum+=digit
    a=a//10
print(sum)
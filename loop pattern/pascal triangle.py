a=int(input("enter a number:"))
i=a
rev=0
while a>0:
    rev=(rev*10)+a%10
    a=a//10
if i==rev:
    print("it id=s palindrome")
else:
    print("not palindrime")


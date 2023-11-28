n=int(input())
a=[]
for i in range(n):
    val=input()
    a.append(val)
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("not palindrome")
def sumofdigit(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumofdigit(n//10)
n=int(input("enter a number:"))
print(sumofdigit(n))
    
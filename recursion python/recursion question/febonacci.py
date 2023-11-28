# def  febonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return (febonacci(n-1)+febonacci(n-2))
# n=int(input("enter a number:"))
# print(febonacci(n)) 

def fib(n) :
    if n==0 :
        return 0
    elif n ==1 :
        return 1
    else :
        return fib(n-1) +fib(n-2)
n=int(input("enter a number:"))
print(fib(n))

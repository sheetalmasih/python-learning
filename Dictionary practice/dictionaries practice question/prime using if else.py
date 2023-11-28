num=int(input())
p=((2**num)-1)%num
if p==1:
    print("prime")
else:
    print("not prime")
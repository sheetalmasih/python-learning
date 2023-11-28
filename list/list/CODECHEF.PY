T=int(input())
i=0
while i<T:
    X=int(input())
    if X<300:
        print(300*10)
    else:
        print(X*10)
    i+=1

T=int(input('ENTTER A NUMBRT'))
i=0
while i<T:
    A,B,C=map(int,input().split())
    if (A+B)/2>C:
        print("YES")
    else:
        print("NO")
    i+=1
        
t=int (input())      
i=0
while i<T:
    N,M=map(int,input().split())
    if N%M==0 and (N//M)%2==0:
        print("YES")
    else:
        print("NO")
    i+=1

    

    

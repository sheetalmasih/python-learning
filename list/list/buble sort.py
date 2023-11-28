l=int(input())
a=[]
for i in range(l):
    val=int(input())
    a.append(val)
for i in range(l):
    for j in range(l-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print(a)
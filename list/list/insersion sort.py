x=[8,5,9,2,4,0,1,4,2]
for i in range(1,len(x)):
    c=i
    while c>0 and x[c]<x[c-1]:
        a=x[c]
        x[c]=x[c-1]
        x[c-1]=a
        c-=1
print(x)
        
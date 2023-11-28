l1=[8,4,7,2,0]
l2=[2,7,4,1,0]
l3=l1+l2
list=[]
for i in range(len(l3)):
    for j in range(len(l3)):
        if l3[i]>l3[j]:
            a=l3[i]
            l3[i]=l3[j]
            l3[j]=a
    list.append(l3)
print(list)
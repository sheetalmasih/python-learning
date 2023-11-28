num=[5,3,8,6,7,2]
i=0
while i<5:
    min=i
    j=i
    while j<6:
        if num[j]<num[min]:
            min=j
        j+=1
    temp=num[i]
    num[i]=num[min]
    num[min]=temp
    # print(num)
    i+=1
print(num)

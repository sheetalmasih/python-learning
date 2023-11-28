l=int(input())
a=[]
for i in range(l):
    val=int(input())
    a.append(val)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
           print("duplicate number",a[j])
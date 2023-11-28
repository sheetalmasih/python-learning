n=int(input("enter a number"))
f=open('q.8.txt','r')
s=f.read()
lst=s.split()
for i in lst:
    if (len(i)>n):
        print(i)
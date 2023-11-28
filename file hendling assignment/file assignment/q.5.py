# 5. Write a Python program to read a file line by line and store it into a list.
f=open('q.5.txt','r')
a=f.readlines()
l=[]
for i in a :
    l.append(i)
print(l)
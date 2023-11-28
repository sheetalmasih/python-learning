# 7. Write a program to store a matrix into a nested list. (Matrix in a text file) 
f=open('q.7.txt','r')
l=[]
for i in f.readlines():
    a=list(map(int,i.split()))
    l.append(a)
print(l)


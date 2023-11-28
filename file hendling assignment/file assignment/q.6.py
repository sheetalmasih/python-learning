# 6. Write a Python program to read a file line by line and store it into a string variable.
f=open('q.6.txt','r')
a=f.readlines()
s=""
for i in a:
    s+=i
print((s))
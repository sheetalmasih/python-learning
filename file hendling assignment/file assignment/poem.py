f=open("poem.txt","r")
t=f.read()
a=input()
if a in t:
    print("this  is present")
else:
    print("this is not present")
f.close

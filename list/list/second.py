a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b:
  if a<c:
   print(a)
  elif b>c:
   print(b)
  else: 
   print(c)
elif a<b:
    if a>c:
     print(a)
    elif b<c:
     print(b)
    else:
     print(c)
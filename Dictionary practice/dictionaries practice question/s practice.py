a=['apple','mango','guava','papaya']
s=a[1]
s1=a[2]
k=s[::-1]
k1=s1[::-1]
a[1]=k
a[2]=k1
print(a)
###################################################

# a=input()
# b=input()
# a1=len(a)
# b1=len(b)
# if a1<b1:
#     print(a,b,a)
# elif b1<a1:
#     print(b,a,b)
# elif a1==b1:
#     print("invalid")
######################################################

# sibling = {'sheetal masih':18,'shaan masih':25}
# for x, v in sibling.items():
#     sibling = x.replace(' ', '')
#     print (sibling)
###############################################################

# sibling={'sheetal masih':18,'shaan masih':25}
# sibling={x.replace(' ',''):v for x,v in sibling.items()}
# print(sibling)
################################################################

# string="sheetal masih"
# newstring=string.replace(" ","")
# print(newstring)
##################################################################

# string="sheetal shahil"
# new=" "
# for i in string  :
#     if i!=" ":
#        new+=i
# print(new)
###################################################################

# string="sheetal shahil"
# new="".join(string.split())
# print(new)
####################################################################

# str1="sky is blue"
# new=str1.split()
# new=new[::-1]
# new="  ".join(new)
# print(new)
####################################################################

# l=[1,2,4,66,7,5,4,4,3,7,9,6,54,6,75,43,6,7]
# l2=[]
# for i in l:
#     if l.count(i)==1:
#        l2.append(i)
# print(l2)
####################################################################

# string=input("enter a value:")
# em=""
# for i in string:
#     if i.isalpha():
#         var=i
#     else:
#         num=int(i)
#         em=em+(num*var)
# print(em)
####################################################################

# count=1
# def family(name):
#     global count
#     if count<=5:
#         print(name)
#         count+=1
#         family(name)
# family("preeti\nshaan")
############################################################
 
       
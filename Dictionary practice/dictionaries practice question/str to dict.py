# s=input()
# dict={}
# for i in s:
#     keys=dict.keys()
#     if i in keys:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)


##########################################
# a=input()
# b=input()
# new_a = b[:2] + a[2:]
# new_b = a[:2] + b[2:]
# print(new_a + ' ' + new_b)

###################################
# st=input()
# length = len(st)
# if length > 2:
#     if st[-3:] == 'ing':
#       st += 'ly'
#     else:
#       st+= 'ing'
# print(st)
########################################
# s=input("enter a char")
# l=len(s)
# print(l)

########################################

# str=input("enter a char:")
# n=int(input("enter a number:"))
# first_part = str[:n] 
# last_part = str[n+1:]
# print(first_part + last_part)

##############################################

# str=input()
# re=""
# res=""
# for i in range(len(str)):
#     if i%2==1:
#         re=re+str[i]
#     elif i%2==0:
#         res+=str[i]
# print(re)
# print(res)
#####################################################
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# odd = 0
# even = 0
# for x in numbers:
#     if x % 2==0:
#     	even+=1
#     else:
#     	odd+=1
# print("Number of even numbers :",even)
# print("Number of odd numbers :",odd)
#############################################################

# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str);

#############################################################
# str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or (column == 1 and (row == 1 or row == 2 or row == 6)) or (column == 5 and (row == 0 or row == 4 or row == 5))):  
#             str=str+"*"    
#         else:      
#             str=str+" "    
#     str=str+"\n"    
# print(str);

############################################################################
# l=[12,[23], 24,[23,56,[67,[65,[56]],[34,[4343,[45,[56,[43,[65]]]]]]]]]
# output = []
# def reemovNestings(l):
#     for i in l:
#         if type(i) == list:
#             reemovNestings(i)
#         else:
#             output.append(i)
# print('The original list: ', l)
# reemovNestings(l)
# print('The list after removing nesting: ', output)

############################################################
# str1=input("enter a element")
# rstr1 = ''
# index = len(str1)
# while index > 0:
#     rstr1 += str1[ index - 1 ]
#     index = index - 1
# print(rstr1)

#########################################################
# sample_dict = {
#     'Physics': 82,
#     'Math': 65,
#     'history': 75
# }
# print(min(sample_dict, key=sample_dict.get))

###########################################################

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500}
# }
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)
############################################
# l=[2,4,6,8,2,3,4]
# sum=0
# for i in range(len(l)):
#     sum+=l[i]
# print(sum)

######################################################################
# l=[2,4,6,8,2,3,4]
# sum=1
# for i in range(len(l)):
#     sum=sum*l[i]
# print(sum)
#################################################################
# l=[5,7,3,8,6,4,23,6,7]
# max=l[0]
# for i in l :
#     if i > max:
#         max = i
# print(max)

##########################################################
# l=[6,9,2,5,8,4]
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print(min)
###########################################################
# list=['abc', 'xyz', 'aba', '1221','86698']
# ctr = 0
# for i in list:
#     if len(i) > 1 and i[0] == i[-1]:
#       ctr += 1
# print(ctr)
################################################################
# list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# list.sort()
# print(list)
###################################################################
# list=[7,8,9,4,3,6,7,2,1]
# dup= set(list)
# uniq= []
# for x in list:
#     if x not in dup:
#         uniq.append(x)
# print(dup)     
###################################################################

list=[76,8,4]
if not list:
    print("it is empty")
else:
    print("not empty")
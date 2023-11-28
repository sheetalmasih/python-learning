# marks=[10,32,42,65,67,89,76,67]
# total_marks=0
# counter=0
# while counter<len(marks):
#     total_marks=total_marks+marks[counter]
#     counter=counter+1
# print(total_marks)

#.............................................................................
# student_marks=[34,56,45,34,23,67,87,98,67,56,90,64,79,84,35,56]
# length=len(student_marks)
# index=0
# less_than50=0
# more_than50=0
# while index<length:
#     marks=student_marks[index]
#     if marks<50:
#         less_than50+=1
#     else:
#         more_than50+=1
#     index+=1
# print("less than 50",less_than50)
# print("more than 50",more_than50)        

#.......................................................................
# student_name=["shaanu","azad","shaan","adarsh","kunal","nihal","aashu","ayush","ashish"]
# list_length=len(student_name)
# index=0
# while index<list_length:
#     print(student_name[index])
#     index+=1
 #.............................................................................   
# marks=[45,34,21,12,32,12,13,32]
# list=len(marks)
# total_marks=0
# for i in range(list):
#     total_marks=marks[i]+total_marks
# print(total_marks)

#......................................................................
# number=[34,23,42,12,23,112,323]
# count=0
# for i in number:
#     count+=1
# print(count)

#.......................................................................
# num=[10,10,40,40,40,50]
# sum = 0
# for i in num:
#     sum+=i
#     print(i)
# print(sum)

# num=[45,33,23,24,34,28,39,45,65,]
# list=[]
# b=0
# for i in num:
#     if i>20 and i<40:
#         list.append(i)
#         b+=1
# print(list)      
# print(b)

# num=[43,45,34,54,34,23,32,21,21]
# b=0
# for i in num:
#     if i>20 and i<40:
#         print(i)
#         b+=1
#...................................................................
# num=[50,40,23,70,56,12,5,10,7,]
# num.sort()
# print(num)
#...................................................................
# num=[50,40,23,70,56,12,5,10,7]
# max=0
# for i in num:
#     if max<i:
#        max=i  
# print(max)

num=[50,40,23,56,12,5,10,7]
second_max=0
for i in num:
    if second_max<=56:
        second_max=i
print(second_max)
    
# num=[50,40,23,70,56,12,5,10,7]
# new_list=set(num)
# new_list.remove(max(new_list))
# print(max(new_list)) 

        
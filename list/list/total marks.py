student_marks=[10,30,60,70,40,80]
length=len(student_marks)
index=0
total_marks=0
while index<=len(student_marks):
    total_marks=student_marks[index]+total_marks
    index=index+1
    print(str(total_marks))
#.................................................................................
    
# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:
#    marks = student_marks[index]
#    if marks < 50:
#       less_than50 = less_than50 + 1
#    else:
#       more_than50 = more_than50 + 1
#    index = index + 1
# print("Marks more than 50: " + str(more_than50))
# print("Marks less than 50: " + str(less_than50))
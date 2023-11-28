# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# maximum=0
# for i in numbers:
#     if maximum<i:
#         maximum=i
# print(maximum)
#..................................................................
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
second_maximum=0
for i in numbers:
    if i>max:
        second_maximum=max
        max=i
    elif max>second_maximum and second_maximum<i:
        second_maximum=i
print("maxmimum value is:",max)
print("second maximum is:",second_maximum)


# a = int(input("enter num: "))
# b = int(input("enter num: "))
# c = int(input("enter num "))
# if a>b:
#     sec_max=a
# else:
#     sec_max=b
# if sec_max>c:
#     sec_max=c
# print(sec_max)




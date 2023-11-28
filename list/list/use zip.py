# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# z = zip(name, animal, age)
# for name,animal,age in z:
#     print("%s the %s is %s" % (name, animal, age))

# #############################################

# li = [0,25,50,100]
# for i in li:
#     print(i+1,end="  ") 

################################################
# remove nagative elements in list:
def remove(x):
    if x >= 0:
         return True
    else:
        return False
a = [-10, 27, 1000, -1, 0, -30]
for x in filter(remove, a):
     print(x,end=" ")



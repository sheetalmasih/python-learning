# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# sum=0
# for i in range(len(binary_number)):
#     digit=binary_number%[10]
#     sum+=digit*pow[2,i]
#     binary_number//10
# print(sum)

binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
b=0
binary_number.reverse()
for i in range(len(binary_number)):
    b=b+(2**i)*binary_number[i]
print(b)
    
# print(1*1)
# print(1*2)
# print(0*4)
# print(1*8)
# print(1*16)
# print(0*32)
# print(0*64)
# print(1*128)
# print(1+2+8+16+128)

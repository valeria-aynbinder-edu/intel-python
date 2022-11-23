# Write a program that counts the total number of digits
# in a number received from a user using a while loop.

num = int(input("Insert num: "))
digits_num = 0
while num > 0:
    digits_num += 1
    num = num // 10
print(digits_num)
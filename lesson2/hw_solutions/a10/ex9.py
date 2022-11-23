# Reverse a given integer number. Solve the exercise in two ways:
# By converting received number to string and operating on string
# Do not convert the number to string, and use modulus operator

# option 1
num = input('Insert a num: ')
print(num[::-1])

# option 2
num = int(input("Insert a num: "))
while num > 0:
    print(num % 10, end="")
    num = num // 10

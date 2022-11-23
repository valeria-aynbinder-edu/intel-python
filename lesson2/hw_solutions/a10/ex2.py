# Get an integer number from a user, and using a while loop
# print every third number starting from 1 up to the number inserted by the user

num = int(input("Insert an integer num: "))
i = 1
while i <= num:
    print(i)
    i += 3
# Write a program that receives a number from a user and prints a multiplication table of a given number.
n = int(input("Insert a number: "))
for i in range(1, 11):
    product = n * i
    # print(f"{i}*{n} = {product}")
    print(f"{i:5d}*{n} = {product}")
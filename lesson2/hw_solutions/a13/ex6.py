# Find the factorial of a given number.
# Take into account that factorial of 0 is 1,
# and factorial does not exist for negative numbers.

num = int(input("Insert num: "))
if num < 0:
    print("Factorial does not exist")
elif num == 0:
    print("1")
else:
    fact = 1
    for i in range(2, num+1):
        fact *= i
    print(fact)
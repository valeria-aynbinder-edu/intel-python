# Write a number that receives a list of numbers, and finds the second-largest number

nums = [56, 3, 23, 1, 0, 45, -1, 4, 2, 0]
nums = [45, 3, 23, 1, 0, 45, -1, 4, 2, 0]

max_num = None
second_max = None

for n in nums:
    if max_num is None:
        max_num = n
    else:
        if n > max_num:
            second_max = max_num
            max_num = n
        else:
            if second_max is None:
                second_max = n
            else:
                if second_max < n <= max_num:
                    second_max = n

print(second_max)
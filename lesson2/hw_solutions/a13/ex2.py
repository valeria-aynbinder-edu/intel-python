# Write a program that receives a list of numbers, and prints the minimum number
nums = [56, 3, 23, 1, 0, 45, -1, 4, 2, 0]

min_num = None
for i in nums:
    if min_num is None:
        min_num = i
    elif min_num > i:
        min_num = i
print(min_num)


# Ziv' s solution
# num_list = []
# flag = True
# temp = None
#
# while flag:
#     num = input("Enter a number to the list, $ to stop: ")
#     if num == '$':
#         flag = False
#         break
#     else:
#         if not num.isdigit():
#             print("Invalid input. Use numbers.")
#             continue
#         else:
#             num = int(num)
#             num_list.append(num)
#             continue
#
# print(num_list)
#
# for x in range(len(num_list)):
#     if x == 0:
#         temp = num_list[x]
#         continue
#     else:
#         if num_list[x] < num_list[x-1]:
#             temp = num_list
#
# print(temp)